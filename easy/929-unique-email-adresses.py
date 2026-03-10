class Solution(object):
    def numUniqueEmails(self, emails):
        result = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            unique_name = local + "@" + domain
            if unique_name not in result:
                result.add(unique_name)
        return len(result)
