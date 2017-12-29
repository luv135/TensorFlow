strings = ["LED_CAMER_ON",
           "LED_CAMER_OFF",
           "LED_SFZ_ON",
           "LED_SFZ_OFF",
           "LED_E7763_FINGER_ON",
           "LED_E7763_FINGER_OFF",
           "LED_OCR_ON",
           "LED_OCR_OFF",
           "PWR_PRINTER_ON",
           "PWR_PRINTER_OFF",
           "LED_BSFZ_ON",
           "LED_BSFZ_OFF",
           "LED_BFINGER_ON",
           "LED_BFINGER_OFF"]


def toBig(s, offset):
    s = s.lower()
    while True:
        offset = s.find("_", offset)
        if offset > 0:
            offset += 1
            s = s.replace(s[offset], s[offset].upper())
        else:
            break
    s = s.replace("_", "")
    return s


for s in strings:
    # print('''
    #  actions.put("%s", "com.unistrong.luowei.%s")
    # ''' % (s, s))
    print('''
            names.put("%s", "%s")
''' % (s, s))

    # print('''
    #  fun %s() {
    #     context.sendBroadcast(Intent("com.unistrong.luowei.%s"))
    # }
    # ''' % (toBig(s, 0), s))
