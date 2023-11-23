import argparse
import os
from classes.staticsite import StaticSite



def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template", default="basic")
    parser.add_argument("-s", "--static", default=".")
    parser.add_argument("-p", "--posts", default="./posts")
    parser.add_argument("-o", "--output", default="./posts")

    args = parser.parse_args()
    

    static_path = os.path.abspath(args.static)
    posts_path = os.path.abspath(args.posts)
    output_path = os.path.abspath(args.output)

    static = StaticSite(
        template=args.template, 
        posts=posts_path, 
        static=static_path,
        output=output_path
    )
    static.generate()


if __name__ == "__main__":
    main()
