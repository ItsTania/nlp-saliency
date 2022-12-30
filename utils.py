import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
import torch

def _register_embedding_list_hook(model, embeddings_list):
    def forward_hook(module, inputs, output):
        embeddings_list.append(output.squeeze(0).clone().cpu().detach().numpy())
    embedding_layer = model.deberta.embeddings.word_embeddings
    handle = embedding_layer.register_forward_hook(forward_hook)
    return handle

def _register_embedding_gradient_hooks(model, embeddings_gradients):
    def hook_layers(module, grad_in, grad_out):
        embeddings_gradients.append(grad_out[0])
    embedding_layer = model.deberta.embeddings.word_embeddings
    hook = embedding_layer.register_backward_hook(hook_layers)
    return hook

def get_saliency_map(model, input_ids, token_type_ids, input_mask):
    torch.enable_grad()
    model.eval()
    embeddings_list = []
    handle = _register_embedding_list_hook(model, embeddings_list)
    embeddings_gradients = []
    hook = _register_embedding_gradient_hooks(model, embeddings_gradients)

    model.zero_grad()
    
    output = model(input_ids, attention_mask=input_mask) 
    output['logits'][0].backward() 

    handle.remove()
    hook.remove()

    saliency_grad = embeddings_gradients[0].detach().cpu().numpy()        
    saliency_grad = np.sum(saliency_grad * embeddings_list[0], axis=-1)
    norm = np.linalg.norm(saliency_grad, ord=1)
    saliency_grad = [e / norm for e in saliency_grad] 
    
    return saliency_grad

def calculate_single_saliency(model, inputs, input_index=0):
    return get_saliency_map(model, inputs['input_ids'][input_index].unsqueeze(0), inputs['token_type_ids'][input_index].unsqueeze(0), inputs['attention_mask'][input_index].unsqueeze(0))

def calculate_saliencies(model, inputs):
    n = len(inputs['input_ids'])
    return [calculate_single_saliency(model, inputs, input_index=i)[0] for i in range(n)]