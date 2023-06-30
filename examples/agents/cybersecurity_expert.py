import os
from log10.llm import Anthropic, OpenAI
from log10.load import log10
from log10.agents.camel import camel_agent
from dotenv import load_dotenv

load_dotenv()

# Select one of OpenAI or Anthropic models
model = "gpt-3.5-turbo-16k"
# model = "claude-1"
max_turns = 30

llm = None
summary_model = None
if "claude" in model:
    summary_model = "claude-1-100k"
    llm = Anthropic({"model": model})
else:
    summary_model = "gpt-3.5-turbo-16k"
    llm = OpenAI({"model": model})

# example calls from playground (select 1)
camel_agent(
    user_role="C developer",
    assistant_role="Cybersecurity expert",
    task_prompt='Correct the following code.\n\n#include <stdio.h>\n#include <string.h>\n\nint main() {\n    char password[8];\n    int granted = 0;\n\n    printf("Enter password: ");\n    scanf("%s", password);\n\n    if (strcmp(password, "password") == 0) {\n        granted = 1;\n    }\n\n    if (granted) {\n        printf("Access granted.\\n");\n    } else {\n        printf("Access denied.\\n");\n    }\n\n    return 0;\n}',
    summary_model=summary_model,
    max_turns=max_turns,
    llm=llm,
)
