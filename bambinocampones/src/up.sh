echo "CLEANUP PREVIOUS EXPORTS"
rm -rf /home/leandro/projects/svn/professionalit/customers/bambinocampones/export/webapps
echo "DONE CLEANUP"
sleep 1
echo "EXPORTING"
svn export /home/leandro/projects/svn/professionalit/customers/bambinocampones/src/webapps /home/leandro/projects/svn/professionalit/customers/bambinocampones/export/webapps
echo "DONE EXPORT"
