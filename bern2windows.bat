@echo off

REM Run GNormPlus
cd resources\GNormPlusJava
start java -Xmx16G -Xms16G -jar GNormPlusServer.main.jar 18895 >> ..\..\logs\nohup_gnormplus.out 2>&1
cd ..

REM Run tmVarJava
cd tmVarJava
start java -Xmx8G -Xms8G -jar tmVar2Server.main.jar 18896 >> ..\..\logs\nohup_tmvar.out 2>&1
cd ..

REM Normalize Disease
cd normalization
start java -Xmx16G -jar normalizers\disease\disease_normalizer_21.jar "inputs\disease" "outputs\disease" "dictionary\dict_Disease_20210630.txt" "normalizers\disease\resources" 9 18892 >> ..\..\logs\nohup_disease_normalize.out 2>&1

cd normalizers\gene

REM Normalize Gene
cd normalization\normalizers\gene
start java -Xmx20G -jar gnormplus-normalization_21.jar 18888 >> ..\..\..\..\logs\nohup_gene_normalize.out 2>&1




