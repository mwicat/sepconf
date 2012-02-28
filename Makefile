DIST=`pwd`/dist
PICKLE=$(DIST)/users.pickle

GENERATE_CMD=python sepgen.py generate
FILL_CMD=cheetah fill --pickle $(PICKLE) --odir dist --oext out --flat -R templates

ASTERISK_PHONES=/etc/asterisk/sccp-phones-auto.conf
FREESWITCH_PHONES=/usr/local/freeswitch/conf/directory/default/sccp-phones-auto.xml

all: init generate fill install_freeswitch install_asterisk

init:
	-mkdir dist

generate: init
	$(GENERATE_CMD) 10 --format csv | cat - custom.csv | ./sepgen.py transform > $(PICKLE)

fill: init
	$(FILL_CMD)

install_asterisk: init
	cp dist/sccp_phones_asterisk.out $(ASTERISK_PHONES)

install_freeswitch: init
	cp dist/sccp_phones_freeswitch.out $(FREESWITCH_PHONES)
