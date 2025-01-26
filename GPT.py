from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Завантаження токенізатора та моделі GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Функція для генерації тексту
def generate_text(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Приклад використання
prompt = "Once upon a time"
generated_text = generate_text(prompt)
print(generated_text)
