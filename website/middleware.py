from django.http import HttpResponseRedirect
import re

class MobileWebsiteMiddleware(object):

    PATTERN = '(iphone|windows ce|mobile|phone|symbian|mini|pda|ipod|mobi|blackberry|playbook|vodafone|kindle)'

    def process_request(self, request):

        if request.META.has_key('HTTP_USER_AGENT'):
            userAgent = request.META.get('HTTP_USER_AGENT')

            reg = re.compile(self.PATTERN, re.IGNORECASE)
            match = reg.search(userAgent)

            if match:
                # mobile browser, check if need to redirect
                path = request.path_info

                if not path.startswith('/m/'):
                    # need to redirect
                    return HttpResponseRedirect('/m' + path)

        return None