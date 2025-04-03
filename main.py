# Script to run the blog writer project

# Warning control
import warnings
warnings.filterwarnings('ignore')

from crew import BlogWriter

def write_blog_post(topic: str):
    # Initialize the crew
    my_writer = BlogWriter()

    # Run
    result = my_writer.crew().kickoff(inputs = {
        'topic': topic
        })
    
    return result


if __name__ == "__main__":

    write_blog_post("Price Optimization")