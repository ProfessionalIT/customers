echo "CLEANUP PREVIOUS EXPORTS"
rm -rf /home/leandro/projects/svn/professionalit/customers/equineclinic/export/equineclinic
echo "DONE CLEANUP"
sleep 1
echo "EXPORTING"
svn export /home/leandro/projects/svn/professionalit/customers/equineclinic/src/equineclinic /home/leandro/projects/svn/professionalit/customers/equineclinic/export/equineclinic
echo "DONE EXPORT"
