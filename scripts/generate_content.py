import google.generativeai as genai
from subject_objects import advanced_database_systems
import markdown
from bs4 import BeautifulSoup
import re
import time

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")

def markdown_to_plain_text(markdown_content):
    html_content = markdown.markdown(markdown_content)
    soup = BeautifulSoup(html_content, "html.parser")
    plain_text = re.sub(r'\n+', '\n', soup.get_text())
    return plain_text

def generate_content(module_name, topic_name):
  prompt = f"""Write a detailed and structured explanation on the following topic in plain text: "{topic_name}" from the module "{module_name}".

    # {topic_name}
  
    Ensure the explanation is thorough where the topic warrants depth but remain concise and focused if the topic has limited scope. 
    The output should prioritize clarity, relevance, and practical understanding. Focus on these aspects:

    1. **Introduction**:
       - Provide a brief and compelling overview of "{topic_name}".
       - Highlight its importance and relevance in the context of "{module_name}".

    2. **Detailed Explanation**:
       - Define and explain "{topic_name}" clearly and succinctly.
       - Expand on its key aspects, mechanisms, or theoretical underpinnings where applicable.
       - Avoid unnecessary elaboration if the topic has limited content, focusing instead on essential points.

    3. **Practical Use Cases and Examples**:
       - Include real-world applications, case studies, or scenarios where "{topic_name}" is relevant.
       - Use comparisons or contrasting examples for better understanding, if applicable.

    4. **Open Source Discussions**:
       - Mention any popular open-source tools, frameworks, or platforms related to "{topic_name}".
       - Explain their role and importance in academic or professional settings.

    5. **Student-Oriented Additions**:
       - Summarize key takeaways and learning objectives for this topic.
       - Highlight common challenges or misconceptions students might face regarding "{topic_name}" and provide actionable tips to overcome them.
       - Suggest resources, tools, or exercises for hands-on learning.

    6. **Current Trends and Future Directions**:
       - Discuss ongoing research, advancements, or innovations related to "{topic_name}".
       - Highlight its potential future applications and impact on technology and society.

    Ensure the content is student-friendly, engaging, and easy to understand. Use code snippets, or examples sparingly but effectively to enhance comprehension when applicable. Tailor the level of detail to the scope of "{topic_name}" to maintain a balance between depth and brevity."""
  response = model.generate_content(prompt)
  return response.text
  plain_text = markdown_to_plain_text(response.text)
  return plain_text
  
i = 1
for module in advanced_database_systems:
    for topic in module[1]:
        result = generate_content(module[0], topic)
        with open(f"module{i}.md", "a") as file:
            file.write(result)
            file.write("\n\n")
        # Sleep for 4 seconds to respect the rate limit of 15 requests per minute
        time.sleep(4)
    i += 1

# result = generate_content("Module 1: Object-Based Databases", "Overview")
# print(result)