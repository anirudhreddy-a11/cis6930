import argparse
import sys
import requests
import json



def main(page=None, file=None):
    # Download data
    if page is not None:
        # TODO Download data function
        response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
    'page': page
        })
        data = json.loads(response.content)
        #print(data['page'])
        #print(data['items'][0]['title'])
        
    
    elif file is not None:       
        # TODO Retrieve the file contents
        with open('data.json', 'r') as file:
            data = json.load(file)
	
    # TODO call formating data function
    itemslist=data['items']
    keys = ['title','subjects','field_offices']
    output = [[item[key] for key in keys if key in item] for item in itemslist]


    #making all the subsets of the list to string 
    result = []
    
    for sublist in output:
        # Flatten each sublist
        flattened_sublist = []
        for item in sublist:
            if isinstance(item, list):
                flattened_sublist.extend([str(i) for i in item])
            elif item in [None, '',[]]:  # Skip None and empty strings
                pass
            else:
                flattened_sublist.append(str(item))
        result.append(flattened_sublist)
    #print(result)    



    # TODO print the thron separated fule
    formatted_output = ''
    thorn = "þ"
    for item in result:
        formatted_output += thorn.join(map(str, item)) + '\n'
    print(formatted_output)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="An Example API file.")
    parser.add_argument("--page", type=int, required=False, help="An Example API file.")
     
    args = parser.parse_args()
    if args.page:
        main(page=args.page)
    elif args.file:
        main(file=args.file)
    else:
        parser.print_help(sys.stderr)