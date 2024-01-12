# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/llemma_34b")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/llemma_34b")