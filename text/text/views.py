from django.http import HttpResponse
from django .shortcuts import render
def index(request):

        dict={ 'name' :'Rohan' ,'place' :'Rohtak' }
        return render(request,'index.html',dict)
def analyse(request):
        #get the text
        djtext=(request.POST.get('text','Default'))
        removepunc=request.POST.get('removepunc','default')
        capitalise=request.POST.get('capitalise','off')
        newlineremover=request.POST.get('newlineremover','off')
        spaceremover=request.POST.get('spaceremover','off')
        charcount=request.POST.get('charcount','off')
        #analyse the text
        analysed=[]
        for w in djtext:
                if (w>='a' and w<='z') or  (w>='A' and w<='Z') or w==" "  :
                   analysed.append(w)
        k=""
        if removepunc=='on':
                for w in analysed:
                        k+=w
                params={'purpose':'remove_punctations','analysed_text':k }
                return render(request, 'analyse.html', params)
        elif capitalise=='on':
                analysed=""
                for w in djtext:
                        if w>='a' and w<='z':
                                m=chr(ord(w)-32)
                                analysed+=(m)
                params={'purpose':'capitalise of letters','analysed_text':analysed}
                return render(request,'analyse.html',params)
        elif newlineremover=='on':
                analysed=""
                for w in djtext:
                        if w !='\n':
                             analysed+=w
                params={'purpose':'Line Remover','analysed_text':analysed}
                return render(request,'analyse.html',params)
        elif spaceremover=='on':
                analysed=""
                for index,w in enumerate(djtext):
                        if djtext[index]==" " and  djtext[index+1]==" ":
                                pass
                        else :
                                analysed+=w
                params={'purpose':'space Remover','analysed_text':analysed}
                return render(request,'analyse.html',params)
        elif charcount=='on':
                count=0
                for w in djtext:
                        if (w>='A' and w<='Z' ) or (w>='a' and w<='z'):
                                count+=1
                params={'purpose':'character counter','analysed_text':count}
                return render(request,'analyse.html',params)