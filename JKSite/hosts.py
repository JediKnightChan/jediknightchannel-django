from django_hosts import patterns, host

host_patterns = patterns('path.to',
    host(r'news', 'news.urls', name='news'),
)