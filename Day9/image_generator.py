import requests
import urllib.parse

disallow_list = "swords, violence, blood, nudity, adult content, weapons"

def build_metaprompt(monument_name):
    meta_prompt = f"""educational illustration for children, safe for work, appropriate for children,
16:9 aspect ratio, bright, clear, historically accurate,
avoid: {disallow_list},
subject: historical monument {monument_name}"""
    return meta_prompt

def generate_image(monument_name, output_file="generated-monument.png"):
    prompt = build_metaprompt(monument_name)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1792&height=1024&nologo=true"
    response = requests.get(url)
    with open(output_file, "wb") as f:
        f.write(response.content)
    print(f"Image saved as {output_file}")

if __name__ == "__main__":
    monument = input("Enter a historical monument name: ")
    generate_image(monument)