def maskify(cc):
  if cc == "":
    return ""
  if len(cc) < 4:
    return cc
  else:
    cc_lst = list(cc)

    cc_end = cc_lst[(len(cc_lst)-4):]

    hashcc = ['#' for c in cc_lst[:(len(cc_lst)-4)]]

    return "".join(hashcc+cc_end)