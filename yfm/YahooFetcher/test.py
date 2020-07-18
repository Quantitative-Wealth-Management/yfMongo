#!/usr/bin/python3

#
# Copyright 2020, Ruben Afonso - http://www.github.com/rubenafo
# Licensed under the Apache License (see the LICENSE file)
#

import YahooFetcher
import ComponentsExtractor

c = ComponentsExtractor.ComponentsExtractor()
#ex = c.getExchange("mse")
ex = c.getExchange("nasdaq")
for e in ex:
  print e
