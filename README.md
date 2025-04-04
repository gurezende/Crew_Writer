# CrewAI Blog Writer Documentation

![](output/Gemini_Generated_ProjectCrew-wide.jpg)

This Python script utilizes the CrewAI framework to automate the creation of a blog post. It defines a crew of agents, each with specific roles, and tasks that guide the workflow from content planning to final editing and illustration.

## Overview

The script sets up a `BlogWriter` class that inherits from `CrewBase`, providing a structured approach to defining agents and tasks. It leverages LLMs (Language Learning Models) and tools like SerperDev and Dall-E to generate content and illustrations.

## Dependencies

-   `warnings`: For suppressing warnings.
-   `os`: For interacting with the operating system.
-   `crewai`: The CrewAI framework for agent collaboration.
-   `crewai.project`: CrewAI project utilities.
-   `crewai.knowledge.source.pdf_knowledge_source`: For reading PDF documents.
-   `crewai_tools`: Tools for web search and image generation.
-   `dotenv`: For loading environment variables from a `.env` file.

## Setup

1.  **Environment Variables:**
    -   Create a `.env` file in the project's root directory.
    -   Add your OpenAI API key as `OPENAI_API_KEY`.
    -   If using `groq`, add your groq API key as `GROQ_API_KEY`.
2.  **Configuration Files:**
    -   Ensure that `config/agents.yaml` and `config/tasks.yaml` exist, defining the agents and tasks configurations.
3.  **PDF Files:**
    -   Place the PDF files (`article1.pdf`, etc.) in the **knowledge** folder or adjust the `file_paths` in `PDFKnowledgeSource`.
4.  **Output Directory:**
    -   An `output` directory will be created by the agents in the root directory to store the generated blog post and image links.

## Code Explanation

1. Initialize PDFKnowledgeSource to read content from PDF files.
2. Initialize the LLM with the specified model and API key.
3. Initialize Dall-E tool for image generation.
4. Defines the BlogWriter class, inheriting from CrewBase.
5. Specifies the paths to agents.yaml and tasks.yaml.
6. Defines agents (writer_style, planner, content_writer, editor, illustrator) with their configurations, tools, and LLMs.
7. Defines tasks (style, plan, write, edit, illustrate) with their configurations and output file paths.
8. Defines the crew method that creates a Crew instance with the specified agents and tasks, using a sequential process.

### Agents
* writer_style: Agent that defines the writing style.
* planner: Agent that plans the blog post structure.
* content_writer: Agent that writes the main content.
* editor: Agent that edits and refines the content.
* illustrator: Agent that generates image links.

### Tasks
* style: Defines the writing style.
* plan: Plans the blog post structure.
* write: Writes the blog post content.
* edit: Edits the blog post.
* illustrate: Generates image links.`

## Running the Agents

Ensure that crew.py and get_image.py are in the same directory or in a directory accessible by Python's import paths.

Run the script:

```bash
python main.py
```

The script will:

* Initialize the BlogWriter crew.
* Generate a blog post based on the provided `topic`.
* Retrieve the generated image.
* The blog post will be saved in output/blog_post.md (as defined in crew.py).
* The image links will be saved in output/picture.txt (as defined in crew.py).
* The inputs dictionary passed to kickoff() is used to provide initial data to the crew's tasks. Ensure that the keys match the expected input parameters in your task definitions.
