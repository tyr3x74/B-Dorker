import urllib, http.client, re, urllib.request, urllib.error, urllib.parse, os
##################################
##       Coded By Tyr3X         ##
## https://github.com/tyr3x74/  ##
##################################
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')]
sitelist = []
web = []
def dorker(dork,pages):
    d = urllib.parse.quote(dork)
    p = 1
    m = pages * 10
    while p <= m:
        try:
            search = "https://www.bing.com/search?q=" + d +"&first=" + str(p) + "&rdr=1&rdrig=7784A68910F94CDE9DFA1DBF740D3A29"
            req = opener.open(search)
            source = req.read().decode('utf8')
            sites = re.findall('<h2><a href="http://(.*?)"', source)
            sitelist.extend(sites)
            p += 10
        except urllib.error.URLError:
            print ("url error")
            continue
        except urllib.request.HTTPError:
            print ("http error")
            continue
        except IOError:
            continue
        except http.client.HTTPException:
            continue
    uniqsites = list(set(sitelist))  
    print ("\n[-] RESULT :")
    for line in uniqsites:
        sep = '/'
        build = "http://" + line.split(sep,1)[0]
        web.append(build)
        print(build)        
    final1 = list(set(web))
    foo = open("result.txt","w")
    for ss in final1:
        foo.write(ss + "\n")
    foo.close()
    print ("\n\nsaved : result.txt")
def main():    
    if os.name == "nt":
         os.system("cls")
    else:
        os.system("clear")
    dorkk = str(input('[+] Type dork : '))
    numpages = int(input('[+] Number of pages to look for : '))
    dorker(dorkk, numpages)

if __name__ == "__main__":
    main()