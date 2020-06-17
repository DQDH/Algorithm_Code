class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        path_spilt = path.split('/')
        for path_i in path_spilt:
            if path_i == '' or path_i == '.':
                continue
            elif path_i == '..':
                if res:
                    res.pop()
            else:
                res.append(path_i)
        return '/' + '/'.join(res) if res else '/'
    def simplifyPath1(self, path):
        """
        :type path: str
        :rtype: str
        """
        res=[]
        path_spilt=path.split('/')
        for path_i in path_spilt:
            if path_i !='' and path_i!='.':
                if path_i=='..':
                    if res:
                        res.pop()
                else:
                    res.append(path_i)
        if not res:
            return '/'
        else:
            return '/'+'/'.join(res)
print(Solution().simplifyPath("/a/../../b/../c//.//"))