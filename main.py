from transformers import GPT2Tokenizer, GPT2LMHeadModel

def main():
    # 加载预训练模型和分词器
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # 输入文本
    input_text = "The quick brown fox"
    # 对输入进行编码以适应模型
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # 生成文本
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)

    # 解码并打印输出文本
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(output_text)

if __name__ == "__main__":
    main()
