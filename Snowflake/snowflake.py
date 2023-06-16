import pandas as pd


# I only tried the Snowflake part at the end because I have no experience in this field and wanted to concentrate on
# what I knew how to do first. Although I don't have much experience in this field, I think I could still have passed
# this part with more time, as the statement doesn't really seem complicated.
# I think that by the end of my work-study period at Fortuneo, I'll be able to build up my skills on Snowflake.
# In fact, it's already on my to-do list, as I've noticed that it's a technology that comes up a lot in a data stack.


class Snowflake():
    def query(text: str) -> pd.DataFrame:
        # Some code to execute queries against snowflake database
        pass


class SnowflakeQuery():

    def __init__(self, query: str, binary_file_name: str):
        # Fill this function here
        pass

    # Fill any more code you need to allow the object to get pickled and stored in a binary file
    # It could be a helper function or anything else to make the pickling process easy
    # example
    # def store(self):
    # pass


def take_user_query():
    file_name = input("Hello, could you please provide the name of the file for your query, the file will be stored on "
                      "your machine.\n")

    print("Could you please provide the query? The query definition will end with ';'")
    query = []
    while True:
        line = input()
        if line.endswith(';'):
            query.append(line)
            break
        query.append(line)

    # Save the query to the file
    with open(file_name, 'w') as file:
        file.write('\n'.join(query))

    # Display a confirmation message to the user
    print(f"Thank you, your query has been registered under the file name {file_name}")


if __name__ == '__main__':
    take_user_query()
