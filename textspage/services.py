from django.core.paginator import Paginator
from .models import Text
from django.db.models import Q


class TextService:
    @staticmethod
    def get_filtered_texts(request):
        params = TextService._extract_params(request)
        queryset = TextService._apply_filters(Text.objects.all(), params)
        return TextService._paginate_queryset(queryset, request.GET.get('page'))

    @staticmethod
    def _extract_params(request):
        return {
            'sort': request.GET.get('sort', 'newest'),
            'level': request.GET.get('level', 'all'),
            'search': request.GET.get('search', ''),
        }

    @staticmethod
    def _apply_filters(queryset, params):
        queryset = TextService._filter_by_level(queryset, params['level'])
        queryset = TextService._filter_by_search(queryset, params['search'])
        return TextService._sort_queryset(queryset, params['sort'])

    @staticmethod
    def _filter_by_level(queryset, level):
        if level and level != 'all':
            return queryset.filter(english_level=level)
        return queryset

    @staticmethod
    def _filter_by_search(queryset, search_query):
        if search_query:
            return queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        return queryset

    @staticmethod
    def _sort_queryset(queryset, sort_order):
        if sort_order == 'oldest':
            return queryset.order_by('created_at')
        return queryset.order_by('-created_at')

    @staticmethod
    def _paginate_queryset(queryset, page_number, per_page=10):
        paginator = Paginator(queryset, per_page)
        return paginator.get_page(page_number)

    @staticmethod
    def get_context(page_obj, params):
        return {
            'texts': page_obj,
            'text': Text(),
            'sort_order': params['sort'],
            'active_level': params['level'],
            'search_query': params['search'],
        }