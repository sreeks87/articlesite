from datetime import timedelta
from random import randint,sample
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from .models import PostArticle
from .forms import SearchBar
# Create your views here.


#Function to return the list of artilces from DB to the home page'''
def article_list(request):
	try:
		print ('here4')
		print(request.POST)
		if(request.POST.get('submit')):
			search_result(request)
		else:
			print('no')
		#Selecting articles in desc order of publishing time'''
		articles = PostArticle.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

		#Pagination logic for article list.'''
		paginator = Paginator(articles, 4)
		page = request.GET.get('page')

		#Exception if page num is invalid or not found, returns first page'''
		try:
			articles = paginator.page(page)
		except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
			articles = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			articles = paginator.page(paginator.num_pages)
		random_article = article_random()
		context = {
		'articles' :articles,
		'rand_art' : random_article
		}
		return render(request, 'article/article_list.html', context,context_instance=RequestContext(request))
	except Exception as e:
		print (e)
		context = {error:'Error occured!!!'}
		return render(request,'article/error.html',context)
	


#The below function fetches the details of each article from the table
def article_detail(request,pk):
	print ('here4')
	print(request.POST)
	if(request.POST.get('submit')):
		search_result(request)
	else:
		print('no')	
	article = get_object_or_404(PostArticle, pk=pk)
	context = {
	'article':article
	}
	return render(request, 'article/article_detail.html', context)

#The below function fetches all the articles that belong to same category
def article_cat_fetch(request,cat):
	try:
		print ('here4')
		print(request.POST)
		if(request.POST.get('submit')):
			search_result(request)
		else:
			print('no')	
		articles = PostArticle.objects.filter(article_cat=cat).order_by('pub_date')
		context = {
		'articles' : articles
		}
		return render(request, 'article/article_category.html', context)
	except Exception as e:
		print (e)
		context = {error:'Error occured!!!'}
		return render(request,'article/error.html',context)

#Function to fetch random articles for carousel preview
def article_random():
	random_article = []
	article_cnt = PostArticle.objects.filter().count()
	random_cnt = sample(range(article_cnt),2)
	for i in random_cnt:
		random_article.append(PostArticle.objects.filter().all()[i])
	return random_article


'''Function to fetch the What to read next  session in footer.
The below function is implemented as a custom context function, 
so that the data is available in all the templates. The search bar is also 
passed as a context variable'''
def article_footer(request):
	form = SearchBar(request.POST or None)
	articles_foot = PostArticle.objects.filter(pub_date__lte=timezone.now() + timedelta(days=5)).order_by('pub_date')
	paginator = Paginator(articles_foot, 4)
	page = request.GET.get('page')
	try:
		articles_foot = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		articles_foot = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		articles_foot = paginator.page(paginator.num_pages)
	context_foot = {
	'articles_foot' :articles_foot,
	'form': form
	}
	return {'articles_foot' :articles_foot,'form':form}

'''The below function is required to split the search query keywords
into words.'''
def split_search(query):
	print ('here3')
	words = []
	 # Finding single quote in query
	while '"' in query:
		first = query.find('"')
		second = query.find('"', first_quote + 1)
		search_keys = query[first_quote:second_quote + 1]
		words.append(search_keys.strip('"'))
		query = query.replace(quoted_keywords, ' ')
    # Split the rest by spaces
	words.extend(query.split())
	return words

''' The below function does the actual search for keywords in the article post body text'''
def search_text(words):
	print ('here2')
	article = PostArticle.objects.all()
	for word in words:
		articles = article.filter(body_txt__icontains=word)
	return articles

'''The below function is responsible for rendering the search result page'''
def search_result(request):
	try:
		print ('here')
		posts = []
		context = {}
		if request.method == 'POST':
			form = SearchBar(request.POST or None)
			#print('postscscscs--'+str(posts))
			if form.is_valid():
				searchwords = form.cleaned_data['Search']
				searchwordlist = split_search(searchwords)
				posts = search_text(searchwordlist)
				#print('posts--'+posts)
				if posts:
					context ={posts:'posts'}
					print (posts)
					return render(request,'article/article_search.html',context)
	except Exception as e:
		print(e)
		context = {error:'Error occured!!!'}
		return render(request,'article/error.html',context)