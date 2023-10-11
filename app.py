import streamlit as st
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import contextlib
import io

# Import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create the assistant agent
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})

# Create user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy", code_execution_config={"work_dir": "coding"}
)


def get_agent_response(user_message):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        user_proxy.initiate_chat(assistant, message=user_message)
    return buffer.getvalue()


st.title("LLM Agent Interface")

user_input = st.text_area("Enter your input here:")
if st.button("Run Agent"):
    agent_output = get_agent_response(user_input)
    st.markdown(f"## Output:\n```\n{agent_output}\n```")


# # To run the Streamlit app
# if __name__ == "__main__":
#     st.run()
