# big picture - what is this ? 
# Input: a file like server.log
# Output: insights/statistics about the traffic - who's hitting your api the most, the errors, endpoints

# the purpose is to monitor traffic, detect errors, find most used apis, identify high traffic


# counter is a special dict, that is used to count freq

from collections import Counter

# this function reads and structures raw log data

def parse_log(filepath):
     
     #this will store all parsed logs, each entry = one request
     entries = []

     # opens files safely and close automatically after use
     with open(filepath) as f:
          for line in f:
              
              #split line
              parts = line.strip().split()

              # this part ignore the incomplete or broken lines
              if len(parts) < 5:
                   continue
              
              #Converts raw text → structured dictionary
              entries.append({
                   "ip": parts[0],
                   "method":parts[2],
                   "endpoint": parts[3],
                   "status":parts[4]
               })

     return entries

# real logic is here

def analyze(filepath):
     
     # getting data
     entries = parse_log(filepath)

     #safety check
     if not entries:
          print("No Valid Entries.")
          return
     
     ip_counts = Counter(e["ip"] for e in entries)
     endpoint_counts = Counter(e["endpoint"] for e in entries)

     #sums the code if starts with 4 or 5 the count them as error, understood the 400 and 500 range
     error_count = sum(1 for e in entries if e["status"].startswith(("4", "5")))

     #which endpoints are failing the most
     errors_by_ep = Counter(e["endpoint"] for e in entries if e["status"].startswith(("4", "5")))

     #extract top data
     top_ip, top_ip_count = ip_counts.most_common(1)[0]
     top_ep, top_ep_count = endpoint_counts.most_common(1)[0]

     print("=" * 40)
     print(f"Total requests  : {len(entries)}")
     print(f"Total errors    : {error_count}")
     print(f"Top IP          : {top_ip} ({top_ip_count} requests)")
     print(f"Top endpoint    : {top_ep} ({top_ep_count} requests)")

     print("\nTop 3 endpoints:")
     for ep, count in endpoint_counts.most_common(3):
          print(f" {ep:<25} {count} requests")
          
     print("\nErros by endpoint")
     for ep, count in errors_by_ep.most_common():
          print(f" {ep:<25} {count} errors")

analyze("server.log")          