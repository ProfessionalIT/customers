echo "CLEANUP PREVIOUS EXPORTS"
rm -rf /home/leandro/sources/customers/enveloprint/export/enveloprint
echo "DONE CLEANUP"
sleep 1
echo "EXPORTING"
svn export /home/leandro/sources/customers/enveloprint/src/enveloprint /home/leandro/sources/customers/enveloprint/export/enveloprint
echo "DONE EXPORT"
sleep 1
echo "UPDATING"
python2.7 /home/leandro/python_tools/google_appengine/appcfg.py -e enveloprintsite@gmail.com update /home/leandro/sources/customers/enveloprint/export/enveloprint
echo "DONE UPDATE"
