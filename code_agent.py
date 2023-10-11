from autogen import config_list_from_json
import autogen

# get api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 120}

# create user proxy agent, coder, product manager
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin who will give the idea and run the code provided by Coder.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="ALWAYS",
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)

pm = autogen.AssistantAgent(
    name="product_manager",
    system_message="You will help break down the initial idea into a well scoped requirement for the Coder; Do not involve in future conversations or error fixing",
    llm_config=llm_config,
)

# create group chat
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[])

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# start the conversation
user_proxy.initiate_chat(
    manager,
    message="Build a beautiful landing page for a personal website of a data scientist. Include links in the navbar to Home, Notes, Contact me. Use Next.js and Tailwind CSS only.",
)
