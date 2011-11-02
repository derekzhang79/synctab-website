from django.http import HttpResponseRedirect
import re

class MobileWebsiteMiddleware(object):

    MOBI_REG = re.compile('(iphone|windows ce|mobile|phone|symbian|mini|pda' +
                          '|ipod|mobi|blackberry|playbook|vodafone|kindle)',
                          re.IGNORECASE)

    def process_request(self, request):

        if request.META.has_key('HTTP_USER_AGENT'):
            userAgent = request.META.get('HTTP_USER_AGENT')
            match = self.MOBI_REG.search(userAgent)
            path = request.path_info

            if match:
                # mobile browser, check if need to redirect to mobile
                if not path.startswith('/m/'):
                    # need to redirect
                    return HttpResponseRedirect('/m' + path)
            elif path.startswith('/m/'):
                    # need to redirect to normal version
                    return HttpResponseRedirect(path[2:])

        return None