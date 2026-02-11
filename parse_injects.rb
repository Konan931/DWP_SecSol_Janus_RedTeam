
# parse_injects.rb - simple CSV timeline printer
require 'csv'
rows = CSV.read('injects_master.csv', headers: true)
sorted = rows.sort_by { |r| r['minute'].to_i }
sorted.each do |r|
  puts "%3d' - %s - %s: %s" % [r['minute'].to_i, r['id'], r['phase'], r['message']]
end
