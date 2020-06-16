# note: could have just done `from ip_address import ip_address` to do validation
class Solution:
  def validIPAddress(self, IP: str) -> str:

    # validate one segment of an IPv4 address
    def ipv4_segment_check(segment: str) -> bool:
      if len(segment) < 1:
        return False
      if segment[0] == '0' and len(segment) > 1:
        return False
      if segment[0] == '-':
        return False
      try:
        if int(segment) > 255:
          return False
      except ValueError:
        return False
      return True

    # validate one segment of an IPv6 address
    def ipv6_segment_check(segment: str) -> bool:
      if len(segment) > 4 or len(segment) < 1:
        return False
      if not all([c in string.hexdigits for c in segment]):
        return False
      return True

    # create 2 possibly valid IP addresses
    ipv4 = IP.split('.')
    ipv6 = IP.split(':')

    # check if all segments are valid for either IPv4 or IPv6
    if len(ipv4) == 4 and all(ipv4_segment_check(s) for s in ipv4):
      return 'IPv4'
    if len(ipv6) == 8 and all(ipv6_segment_check(s) for s in ipv6):
      return 'IPv6'
    return 'Neither'
