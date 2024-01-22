import openai

class GPT4CodeAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt, max_tokens=100):
        try:
            response = openai.Completion.create(
                engine="text-davinci-004",  # 或其他 GPT-4 引擎
                prompt=prompt,
                max_tokens=max_tokens
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def main():
        api_key = "YOUR_API_KEY_HERE"  # 替换为您的 API 密钥
        agent = GPT4CodeAgent(api_key)

        prompt = "Translate the following English text to French: 'Hello, how are you?'"
        response = agent.generate_response(prompt)
        print(response)

if __name__ == "__main__":
    GPT4CodeAgent.main()
