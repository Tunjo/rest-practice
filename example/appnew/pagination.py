from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ResultPagePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        _page_size = self.request.query_params.get('page_size')
        if _page_size:
            self.page_size = int(_page_size)
        return Response({
            'total': self.page.paginator.count,
            'per_page': self.page_size,
            'current_page': self.page.number,
            'last_page': self.page.paginator.num_pages,
            'next_page_url': self.get_next_link(),
            'prev_page_url': self.get_previous_link(),
            'from': self.calc_from_page(),
            'to': self.calc_to_page(),
            'data': data

        })

    def calc_from_page(self):
        _from_page = self.page_size * self.page.number - (self.page_size - 1)
        if isinstance(_from_page, tuple):
            return _from_page[0]
        return _from_page

    def calc_to_page(self):
        _to_page = int(self.page_size * self.page.number)
        if isinstance(_to_page, tuple):
            _to = _to_page[0] if _to_page[0] < self.page.paginator.count else self.page.paginator.count
            return _to

        _to = _to_page if _to_page < self.page.paginator.count else self.page.paginator.count
        return _to
