#!/usr/bin/env ruby

regex = /t*/

arg = ARGV[0]
puts arg.scan(regex).join

