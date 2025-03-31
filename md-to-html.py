#! /bin/env python

import sys
import os
import markdown

def convert_markdown_to_html(input_md, output_html):
    if not os.path.isfile(input_md):
        print(f"Error: The file {input_md} does not exist.")
        return
                            
    with open(input_md, "r", encoding="utf-8") as f:
        html_content = markdown.markdown(f.read())
        
        html_content = f"<!DOCTYPE html><html lang=\"fr\"><head><meta charset=\"utf-8\"></head><body> {html_content} </body></html>"
                                                                    
        with open(output_html, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"HTML file generated: {output_html}")
                                                                                        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.md output.html")
    else:
        convert_markdown_to_html(sys.argv[1], sys.argv[2])
                                                                                                                    