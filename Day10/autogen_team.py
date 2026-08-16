import autogen

config_list = [
    {
        "model": "llama3.1",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"
    }
]

llm_config = {"config_list": config_list, "temperature": 0}

coder = autogen.AssistantAgent(
    name="Coder",
    system_message="You write clean secure Python code for the given task.",
    llm_config=llm_config
)

reviewer = autogen.AssistantAgent(
    name="Reviewer",
    system_message="You inspect code for security flaws and suggest fixes before approving.",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5,
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    },
    is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", "")
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, reviewer],
    messages=[],
    max_round=10
)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

if __name__ == "__main__":
    task = "Build a secure Python web scraper that fetches a URL, validates the domain against an allowlist, and handles errors safely. Reviewer must check for SSRF and injection risks before approval. Reply TERMINATE when done."
    user_proxy.initiate_chat(manager, message=task)