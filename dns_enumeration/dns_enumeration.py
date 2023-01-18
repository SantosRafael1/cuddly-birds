import dns.resolver

def dns_enumeration(domain) :
    try:
        resolver = dns.resolver.Resolver()

        #perform DNS query for all record types
        for record_types in ["A", "AAAA", "MX", "NS", "SOA", "TXT"]:
            answers = resolver.resolve(domain, record_types)
            print(f"{record_types} records:")
            for recorde_data in answers:
                print(recorde_data)
    except dns.resolver.NXDOMAIN:
        print(f"{domain} doesn't exists")
    except dns.resolver.NoAnswer:
        print(f"No {record_types} records found for {domain}")


input_dns = str(input("Enter a domain: "))
dns_enumeration(input_dns)






#A = mapping ip
#MX = Mail Exchange, responsible for hadling incoming email for a domain
#NS = Name Servers
#SOA = adm information about DNS's configs
#TXt = contain verification codes and info used by different services