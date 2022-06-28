import argparse # argparse is a built in python package, we add it with an import statement
import boto3

# Define the parser variable to equal argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")

# Add each of the arguments using the parser.add_argument() method
parser.add_argument(
    'I did attend the BET Awards show last night',
    dest="Text",
    type=str,
    help="EN",
    required=True
    )

parser.add_argument(
    '--source-language-code', 
    dest="SourceLanguageCode", 
    type=str, 
    help="The language code for the language of the source text. The language must be a language supported by Amazon Translate.",
    required=True
    )

parser.add_argument(
    '--target-language-code',
    dest="TargetLanguageCode",
    type=str,
    help="The language code requested for the language of the target text. The language must be a language support by Amazon Translate.",
    required=True
    )

# This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
args = parser.parse_args()

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    # vars() is an inbuilt function which returns a dictionary object
    translate_text(**vars(args))

if __name__=="__main__":
    main()
