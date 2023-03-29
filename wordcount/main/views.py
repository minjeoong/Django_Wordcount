from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['text']
    text_list = text.split()
    text_dict = {}
    for word in text_list:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    # print(text_dict)
    words = sorted(text_dict.items(),key = lambda x:x[1], reverse=True)
    return render(request, 'result.html', {'words':words})
    # items 를 하는 이유? : 딕셔너리에서 포문을 통해 리스트를 출력해줘야 하기 때문에 
