# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:33:13 2019

@author: qcheng1
"""

import pandas as pd
import os # File/directory operations
import xlsxwriter # Writing to an excel file using Python
import xlrd # Reading an excel file using Python
import cv2 # Read, display, write an image, using OpenCV
import tensorflow as tf #
import torch # convert a Python list object into a PyTorch tensor using the tensor operation. 
import inspect # inspection
import numpy as np #NumPy’s main object is the homogeneous multidimensional array. 
from skimage import io, filters #Scikit-image is an image processing toolbox for SciPy https://scikit-image.org/
import pandas as pd
import scipy as sp
import sklearn as sk
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
#from sklearn.model_selection import train_test_split #Mahalanobis Distance for Classification Problems

#AccessionNumber	isDecentArtists	artworksLG5	artworksLG10	HueArithmeticAverage	HueCircularAverage	LightnessArithmeticAverage	SaturationArithmeticAverageCylinder	SaturationArithmeticAverageBicone	BrightnessDimensionAverage	BrightnessContrast	RedEntropy	GreenEntropy	BlueEntropy	Entropy	hasKaze	ImageFile	edgesV_1	edgesV_2	edgesV_3	edgesV_4	edgesV_5	edgesV_6	edgesV_7	edgesV_8	edgesV_9	edgesV_10	edgesV_11	edgesV_12	edgesV_13	edgesV_14	edgesV_15	edgesV_16	edgesV_17	edgesV_18	edgesV_19	edgesV_20	edgesV_21	edgesV_22	edgesV_23	edgesV_24	edgesV_25	edgesV_26	edgesV_27	edgesV_28	edgesV_29	edgesV_30	edgesV_31	edgesV_32	edgesV_33	edgesV_34	edgesV_35	edgesV_36	edgesV_37	edgesV_38	edgesV_39	edgesV_40	edgesV_41	edgesV_42	edgesV_43	edgesV_44	edgesV_45	edgesV_46	edgesV_47	edgesV_48	edgesV_49	edgesV_50	edgesV_51	edgesV_52	edgesV_53	edgesV_54	edgesV_55	edgesV_56	edgesV_57	edgesV_58	edgesV_59	edgesV_60	edgesV_61	edgesV_62	edgesV_63	edgesV_64	edgesV_65	edgesV_66	edgesV_67	edgesV_68	edgesV_69	edgesV_70	edgesV_71	edgesV_72	edgesV_73	edgesV_74	edgesV_75	edgesV_76	edgesV_77	edgesV_78	edgesV_79	edgesV_80	edgesV_81	edgesV_82	edgesV_83	edgesV_84	edgesV_85	edgesV_86	edgesV_87	edgesV_88	edgesV_89	edgesV_90	edgesV_91	edgesV_92	edgesV_93	edgesV_94	edgesV_95	edgesV_96	edgesV_97	edgesV_98	edgesV_99	edgesV_100	edgesV_101	edgesV_102	edgesV_103	edgesV_104	edgesV_105	edgesV_106	edgesV_107	edgesV_108	edgesV_109	edgesV_110	edgesV_111	edgesV_112	edgesV_113	edgesV_114	edgesV_115	edgesV_116	edgesV_117	edgesV_118	edgesV_119	edgesV_120	edgesV_121	edgesV_122	edgesV_123	edgesV_124	edgesV_125	edgesV_126	edgesV_127	edgesV_128	edgesV_129	edgesV_130	edgesV_131	edgesV_132	edgesV_133	edgesV_134	edgesV_135	edgesV_136	edgesV_137	edgesV_138	edgesV_139	edgesV_140	edgesV_141	edgesV_142	edgesV_143	edgesV_144	edgesV_145	edgesV_146	edgesV_147	edgesV_148	edgesV_149	edgesV_150	edgesV_151	edgesV_152	edgesV_153	edgesV_154	edgesV_155	edgesV_156	edgesV_157	edgesV_158	edgesV_159	edgesV_160	edgesV_161	edgesV_162	edgesV_163	edgesV_164	edgesV_165	edgesV_166	edgesV_167	edgesV_168	edgesV_169	edgesV_170	edgesV_171	edgesV_172	edgesV_173	edgesV_174	edgesV_175	edgesV_176	edgesV_177	edgesV_178	edgesV_179	edgesV_180	edgesV_181	edgesV_182	edgesV_183	edgesV_184	edgesV_185	edgesV_186	edgesV_187	edgesV_188	edgesV_189	edgesV_190	edgesV_191	edgesV_192	edgesV_193	edgesV_194	edgesV_195	edgesV_196	edgesV_197	edgesV_198	edgesV_199	edgesV_200	edgesV_201	edgesV_202	edgesV_203	edgesV_204	edgesV_205	edgesV_206	edgesV_207	edgesV_208	edgesV_209	edgesV_210	edgesV_211	edgesV_212	edgesV_213	edgesV_214	edgesV_215	edgesV_216	edgesV_217	edgesV_218	edgesV_219	edgesV_220	edgesV_221	edgesV_222	edgesV_223	edgesV_224	edgesV_225	edgesV_226	edgesV_227	edgesV_228	edgesV_229	edgesV_230	edgesV_231	edgesV_232	edgesV_233	edgesV_234	edgesV_235	edgesV_236	edgesV_237	edgesV_238	edgesV_239	edgesV_240	edgesV_241	edgesV_242	edgesV_243	edgesV_244	edgesV_245	edgesV_246	edgesV_247	edgesV_248	edgesV_249	edgesV_250	edgesV_251	edgesV_252	edgesV_253	edgesV_254	edgesV_255	edgesV_256	edgesV_257	edgesV_258	edgesV_259	edgesV_260	edgesV_261	edgesV_262	edgesV_263	edgesV_264	edgesV_265	edgesV_266	edgesV_267	edgesV_268	edgesV_269	edgesV_270	edgesV_271	edgesV_272	edgesV_273	edgesV_274	edgesV_275	edgesV_276	edgesV_277	edgesV_278	edgesV_279	edgesV_280	edgesV_281	edgesV_282	edgesV_283	edgesV_284	edgesV_285	edgesV_286	edgesV_287	edgesV_288	edgesV_289	edgesV_290	edgesV_291	edgesV_292	edgesV_293	edgesV_294	edgesV_295	edgesV_296	edgesV_297	edgesV_298	edgesV_299	edgesV_300	edgesV_301	edgesV_302	edgesV_303	edgesV_304	edgesV_305	edgesV_306	edgesV_307	edgesV_308	edgesV_309	edgesV_310	edgesV_311	edgesV_312	edgesV_313	edgesV_314	edgesV_315	edgesV_316	edgesV_317	edgesV_318	edgesV_319	edgesV_320	edgesV_321	edgesV_322	edgesV_323	edgesV_324	edgesV_325	edgesV_326	edgesV_327	edgesV_328	edgesV_329	edgesV_330	edgesV_331	edgesV_332	edgesV_333	edgesV_334	edgesV_335	edgesV_336	edgesV_337	edgesV_338	edgesV_339	edgesV_340	edgesV_341	edgesV_342	edgesV_343	edgesV_344	edgesV_345	edgesV_346	edgesV_347	edgesV_348	edgesV_349	edgesV_350	edgesV_351	edgesV_352	edgesV_353	edgesV_354	edgesV_355	edgesV_356	edgesV_357	edgesV_358	edgesV_359	edgesV_360	edgesV_361	edgesV_362	edgesV_363	edgesV_364	edgesV_365	edgesV_366	edgesV_367	edgesV_368	edgesV_369	edgesV_370	edgesV_371	edgesV_372	edgesV_373	edgesV_374	edgesV_375	edgesV_376	edgesV_377	edgesV_378	edgesV_379	edgesV_380	edgesV_381	edgesV_382	edgesV_383	edgesV_384	edgesV_385	edgesV_386	edgesV_387	edgesV_388	edgesV_389	edgesV_390	edgesV_391	edgesV_392	edgesV_393	edgesV_394	edgesV_395	edgesV_396	edgesV_397	edgesV_398	edgesV_399	edgesV_400	edgesV_401	edgesV_402	edgesV_403	edgesV_404	edgesV_405	edgesV_406	edgesV_407	edgesV_408	edgesV_409	edgesV_410	edgesV_411	edgesV_412	edgesV_413	edgesV_414	edgesV_415	edgesV_416	edgesV_417	edgesV_418	edgesV_419	edgesV_420	edgesV_421	edgesV_422	edgesV_423	edgesV_424	edgesV_425	edgesV_426	edgesV_427	edgesV_428	edgesV_429	edgesV_430	edgesV_431	edgesV_432	edgesV_433	edgesV_434	edgesV_435	edgesV_436	edgesV_437	edgesV_438	edgesV_439	edgesV_440	edgesV_441	edgesV_442	edgesV_443	edgesV_444	edgesV_445	edgesV_446	edgesV_447	edgesV_448	edgesV_449	edgesV_450	edgesV_451	edgesV_452	edgesV_453	edgesV_454	edgesV_455	edgesV_456	edgesV_457	edgesV_458	edgesV_459	edgesV_460	edgesV_461	edgesV_462	edgesV_463	edgesV_464	edgesV_465	edgesV_466	edgesV_467	edgesV_468	edgesV_469	edgesV_470	edgesV_471	edgesV_472	edgesV_473	edgesV_474	edgesV_475	edgesV_476	edgesV_477	edgesV_478	edgesV_479	edgesV_480	edgesV_481	edgesV_482	edgesV_483	edgesV_484	edgesV_485	edgesV_486	edgesV_487	edgesV_488	edgesV_489	edgesV_490	edgesV_491	edgesV_492	edgesV_493	edgesV_494	edgesV_495	edgesV_496	edgesV_497	edgesV_498	edgesV_499	edgesV_500	edgesV_501	edgesV_502	edgesV_503	edgesV_504	edgesV_505	edgesV_506	edgesV_507	edgesV_508	edgesV_509	edgesV_510	edgesV_511	edgesV_512	edgesV_513	edgesV_514	edgesV_515	edgesV_516	edgesV_517	edgesV_518	edgesV_519	edgesV_520	edgesV_521	edgesV_522	edgesV_523	edgesV_524	edgesV_525	edgesV_526	edgesV_527	edgesV_528	edgesV_529	edgesV_530	edgesV_531	edgesV_532	edgesV_533	edgesV_534	edgesV_535	edgesV_536	edgesV_537	edgesV_538	edgesV_539	edgesV_540	edgesV_541	edgesV_542	edgesV_543	edgesV_544	edgesV_545	edgesV_546	edgesV_547	edgesV_548	edgesV_549	edgesV_550	edgesV_551	edgesV_552	edgesV_553	edgesV_554	edgesV_555	edgesV_556	edgesV_557	edgesV_558	edgesV_559	edgesV_560	edgesV_561	edgesV_562	edgesV_563	edgesV_564	edgesV_565	edgesV_566	edgesV_567	edgesV_568	edgesV_569	edgesV_570	edgesV_571	edgesV_572	edgesV_573	edgesV_574	edgesV_575	edgesV_576	edgesV_577	edgesV_578	edgesV_579	edgesV_580	edgesV_581	edgesV_582	edgesV_583	edgesV_584	edgesV_585	edgesV_586	edgesV_587	edgesV_588	edgesV_589	edgesV_590	edgesV_591	edgesV_592	edgesV_593	edgesV_594	edgesV_595	edgesV_596	edgesV_597	edgesV_598	edgesV_599	edgesV_600	edgesV_601	edgesV_602	edgesV_603	edgesV_604	edgesV_605	edgesV_606	edgesV_607	edgesV_608	edgesV_609	edgesV_610	edgesV_611	edgesV_612	edgesV_613	edgesV_614	edgesV_615	edgesV_616	edgesV_617	edgesV_618	edgesV_619	edgesV_620	edgesV_621	edgesV_622	edgesV_623	edgesV_624	edgesV_625	edgesV_626	edgesV_627	edgesV_628	edgesV_629	edgesV_630	edgesV_631	edgesV_632	edgesV_633	edgesV_634	edgesV_635	edgesV_636	edgesV_637	edgesV_638	edgesV_639	edgesV_640	edgesV_641	edgesV_642	edgesV_643	edgesV_644	edgesV_645	edgesV_646	edgesV_647	edgesV_648	edgesV_649	edgesV_650	edgesV_651	edgesV_652	edgesV_653	edgesV_654	edgesV_655	edgesV_656	edgesV_657	edgesV_658	edgesV_659	edgesV_660	edgesV_661	edgesV_662	edgesV_663	edgesV_664	edgesV_665	edgesV_666	edgesV_667	edgesV_668	edgesV_669	edgesV_670	edgesV_671	edgesV_672	edgesV_673	edgesV_674	edgesV_675	edgesV_676	edgesV_677	edgesV_678	edgesV_679	edgesV_680	edgesV_681	edgesV_682	edgesV_683	edgesV_684	edgesV_685	edgesV_686	edgesV_687	edgesV_688	edgesV_689	edgesV_690	edgesV_691	edgesV_692	edgesV_693	edgesV_694	edgesV_695	edgesV_696	edgesV_697	edgesV_698	edgesV_699	edgesV_700	edgesV_701	edgesV_702	edgesV_703	edgesV_704	edgesV_705	edgesV_706	edgesV_707	edgesV_708	edgesV_709	edgesV_710	edgesV_711	edgesV_712	edgesV_713	edgesV_714	edgesV_715	edgesV_716	edgesV_717	edgesV_718	edgesV_719	edgesV_720	edgesV_721	edgesV_722	edgesV_723	edgesV_724	edgesV_725	edgesV_726	edgesV_727	edgesV_728	edgesV_729	edgesV_730	edgesV_731	edgesV_732	edgesV_733	edgesV_734	edgesV_735	edgesV_736	edgesV_737	edgesV_738	edgesV_739	edgesV_740	edgesV_741	edgesV_742	edgesV_743	edgesV_744	edgesV_745	edgesV_746	edgesV_747	edgesV_748	edgesV_749	edgesV_750	edgesV_751	edgesV_752	edgesV_753	edgesV_754	edgesV_755	edgesV_756	edgesV_757	edgesV_758	edgesV_759	edgesV_760	edgesV_761	edgesV_762	edgesV_763	edgesV_764	edgesV_765	edgesV_766	edgesV_767	edgesV_768	edgesV_769	edgesV_770	edgesV_771	edgesV_772	edgesV_773	edgesV_774	edgesV_775	edgesV_776	edgesV_777	edgesV_778	edgesV_779	edgesV_780	edgesV_781	edgesV_782	edgesV_783	edgesV_784	edgesV_785	edgesV_786	edgesV_787	edgesV_788	edgesV_789	edgesV_790	edgesV_791	edgesV_792	edgesV_793	edgesV_794	edgesV_795	edgesV_796	edgesV_797	edgesV_798	edgesV_799	edgesV_800	edgesV_801	edgesV_802	edgesV_803	edgesV_804	edgesV_805	edgesV_806	edgesV_807	edgesV_808	edgesV_809	edgesV_810	edgesV_811	edgesV_812	edgesV_813	edgesV_814	edgesV_815	edgesV_816	edgesV_817	edgesV_818	edgesV_819	edgesV_820	edgesV_821	edgesV_822	edgesV_823	edgesV_824	edgesV_825	edgesV_826	edgesV_827	edgesV_828	edgesV_829	edgesV_830	edgesV_831	edgesV_832	edgesV_833	edgesV_834	edgesV_835	edgesV_836	edgesV_837	edgesV_838	edgesV_839	edgesV_840	edgesV_841	edgesV_842	edgesV_843	edgesV_844	edgesV_845	edgesV_846	edgesV_847	edgesV_848	edgesV_849	edgesV_850	edgesV_851	edgesV_852	edgesV_853	edgesV_854	edgesV_855	edgesV_856	edgesV_857	edgesV_858	edgesV_859	edgesV_860	edgesV_861	edgesV_862	edgesV_863	edgesV_864	edgesV_865	edgesV_866	edgesV_867	edgesV_868	edgesV_869	edgesV_870	edgesV_871	edgesV_872	edgesV_873	edgesV_874	edgesV_875	edgesV_876	edgesV_877	edgesV_878	edgesV_879	edgesV_880	edgesV_881	edgesV_882	edgesV_883	edgesV_884	edgesV_885	edgesV_886	edgesV_887	edgesV_888	edgesV_889	edgesV_890	edgesV_891	edgesV_892	edgesV_893	edgesV_894	edgesV_895	edgesV_896	edgesV_897	edgesV_898	edgesV_899	edgesV_900	edgesV_901	edgesV_902	edgesV_903	edgesV_904	edgesV_905	edgesV_906	edgesV_907	edgesV_908	edgesV_909	edgesV_910	edgesV_911	edgesV_912	edgesV_913	edgesV_914	edgesV_915	edgesV_916	edgesV_917	edgesV_918	edgesV_919	edgesV_920	edgesV_921	edgesV_922	edgesV_923	edgesV_924	edgesV_925	edgesV_926	edgesV_927	edgesV_928	edgesV_929	edgesV_930	edgesV_931	edgesV_932	edgesV_933	edgesV_934	edgesV_935	edgesV_936	edgesV_937	edgesV_938	edgesV_939	edgesV_940	edgesV_941	edgesV_942	edgesV_943	edgesV_944	edgesV_945	edgesV_946	edgesV_947	edgesV_948	edgesV_949	edgesV_950	edgesV_951	edgesV_952	edgesV_953	edgesV_954	edgesV_955	edgesV_956	edgesV_957	edgesV_958	edgesV_959	edgesV_960	edgesV_961	edgesV_962	edgesV_963	edgesV_964	edgesV_965	edgesV_966	edgesV_967	edgesV_968	edgesV_969	edgesV_970	edgesV_971	edgesV_972	edgesV_973	edgesV_974	edgesV_975	edgesV_976	edgesV_977	edgesV_978	edgesV_979	edgesV_980	edgesV_981	edgesV_982	edgesV_983	edgesV_984	edgesV_985	edgesV_986	edgesV_987	edgesV_988	edgesV_989	edgesV_990	edgesV_991	edgesV_992	edgesV_993	edgesV_994	edgesV_995	edgesV_996	edgesV_997	edgesV_998	edgesV_999	edgesV_1000	edgesV_1001	edgesV_1002	edgesV_1003	edgesV_1004	edgesV_1005	edgesV_1006	edgesV_1007	edgesV_1008	edgesV_1009	edgesV_1010	edgesV_1011	edgesV_1012	edgesV_1013	edgesV_1014	edgesV_1015	edgesV_1016	edgesV_1017	edgesV_1018	edgesV_1019	edgesV_1020	edgesV_1021	edgesV_1022	edgesV_1023	edgesV_1024	edgesV_1025	edgesV_1026	edgesV_1027	edgesV_1028	edgesV_1029	edgesV_1030	edgesV_1031	edgesV_1032	edgesV_1033	edgesV_1034	edgesV_1035	edgesV_1036	edgesV_1037	edgesV_1038	edgesV_1039	edgesV_1040	edgesV_1041	edgesV_1042	edgesV_1043	edgesV_1044	edgesV_1045	edgesV_1046	edgesV_1047	edgesV_1048	edgesV_1049	edgesV_1050	edgesV_1051	edgesV_1052	edgesV_1053	edgesV_1054	edgesV_1055	edgesV_1056	edgesV_1057	edgesV_1058	edgesV_1059	edgesV_1060	edgesV_1061	edgesV_1062	edgesV_1063	edgesV_1064	edgesV_1065	edgesV_1066	edgesV_1067	edgesV_1068	edgesV_1069	edgesV_1070	edgesV_1071	edgesV_1072	edgesV_1073	edgesV_1074	edgesV_1075	edgesV_1076	edgesV_1077	edgesV_1078	edgesV_1079	edgesV_1080	edgesV_1081	edgesV_1082	edgesV_1083	edgesV_1084	edgesV_1085	edgesV_1086	edgesV_1087	edgesV_1088	edgesV_1089	edgesV_1090	edgesV_1091	edgesV_1092	edgesV_1093	edgesV_1094	edgesV_1095	edgesV_1096	edgesV_1097	edgesV_1098	edgesV_1099	edgesV_1100	edgesV_1101	edgesV_1102	edgesV_1103	edgesV_1104	edgesV_1105	edgesV_1106	edgesV_1107	edgesV_1108	edgesV_1109	edgesV_1110	edgesV_1111	edgesV_1112	edgesV_1113	edgesV_1114	edgesV_1115	edgesV_1116	edgesV_1117	edgesV_1118	edgesV_1119	edgesV_1120	edgesV_1121	edgesV_1122	edgesV_1123	edgesV_1124	edgesV_1125	edgesV_1126	edgesV_1127	edgesV_1128	edgesV_1129	edgesV_1130	edgesV_1131	edgesV_1132	edgesV_1133	edgesV_1134	edgesV_1135	edgesV_1136	edgesV_1137	edgesV_1138	edgesV_1139	edgesV_1140	edgesV_1141	edgesV_1142	edgesV_1143	edgesV_1144	edgesV_1145	edgesV_1146	edgesV_1147	edgesV_1148	edgesV_1149	edgesV_1150	edgesV_1151	edgesV_1152	edgesV_1153	edgesV_1154	edgesV_1155	edgesV_1156	edgesV_1157	edgesV_1158	edgesV_1159	edgesV_1160	edgesV_1161	edgesV_1162	edgesV_1163	edgesV_1164	edgesV_1165	edgesV_1166	edgesV_1167	edgesV_1168	edgesV_1169	edgesV_1170	edgesV_1171	edgesV_1172	edgesV_1173	edgesV_1174	edgesV_1175	edgesV_1176	edgesV_1177	edgesV_1178	edgesV_1179	edgesV_1180	edgesV_1181	edgesV_1182	edgesV_1183	edgesV_1184	edgesV_1185	edgesV_1186	edgesV_1187	edgesV_1188	edgesV_1189	edgesV_1190	edgesV_1191	edgesV_1192	edgesV_1193	edgesV_1194	edgesV_1195	edgesV_1196	edgesV_1197	edgesV_1198	edgesV_1199	edgesV_1200	edgesV_1201	edgesV_1202	edgesV_1203	edgesV_1204	edgesV_1205	edgesV_1206	edgesV_1207	edgesV_1208	edgesV_1209	edgesV_1210	edgesV_1211	edgesV_1212	edgesV_1213	edgesV_1214	edgesV_1215	edgesV_1216	edgesV_1217	edgesV_1218	edgesV_1219	edgesV_1220	edgesV_1221	edgesV_1222	edgesV_1223	edgesV_1224	edgesV_1225	edgesV_1226	edgesV_1227	edgesV_1228	edgesV_1229	edgesV_1230	edgesV_1231	edgesV_1232	edgesV_1233	edgesV_1234	edgesV_1235	edgesV_1236	edgesV_1237	edgesV_1238	edgesV_1239	edgesV_1240	edgesV_1241	edgesV_1242	edgesV_1243	edgesV_1244	edgesV_1245	edgesV_1246	edgesV_1247	edgesV_1248	edgesV_1249	edgesV_1250	edgesV_1251	edgesV_1252	edgesV_1253	edgesV_1254	edgesV_1255	edgesV_1256	edgesV_1257	edgesV_1258	edgesV_1259	edgesV_1260	edgesV_1261	edgesV_1262	edgesV_1263	edgesV_1264	edgesV_1265	edgesV_1266	edgesV_1267	edgesV_1268	edgesV_1269	edgesV_1270	edgesV_1271	edgesV_1272	edgesV_1273	edgesV_1274	edgesV_1275	edgesV_1276	edgesV_1277	edgesV_1278	edgesV_1279	edgesV_1280	edgesV_1281	edgesV_1282	edgesV_1283	edgesV_1284	edgesV_1285	edgesV_1286	edgesV_1287	edgesV_1288	edgesV_1289	edgesV_1290	edgesV_1291	edgesV_1292	edgesV_1293	edgesV_1294	edgesV_1295	edgesV_1296	edgesV_1297	edgesV_1298	edgesV_1299	edgesV_1300	edgesV_1301	edgesV_1302	edgesV_1303	edgesV_1304	edgesV_1305	edgesV_1306	edgesV_1307	edgesV_1308	edgesV_1309	edgesV_1310	edgesV_1311	edgesV_1312	edgesV_1313	edgesV_1314	edgesV_1315	edgesV_1316	edgesV_1317	edgesV_1318	edgesV_1319	edgesV_1320	edgesV_1321	edgesV_1322	edgesV_1323	edgesV_1324	edgesV_1325	edgesV_1326	edgesV_1327	edgesV_1328	edgesV_1329	edgesV_1330	edgesV_1331	edgesV_1332	edgesV_1333	edgesV_1334	edgesV_1335	edgesV_1336	edgesV_1337	edgesV_1338	edgesV_1339	edgesV_1340	edgesV_1341	edgesV_1342	edgesV_1343	edgesV_1344	edgesV_1345	edgesV_1346	edgesV_1347	edgesV_1348	edgesV_1349	edgesV_1350	edgesV_1351	edgesV_1352	edgesV_1353	edgesV_1354	edgesV_1355	edgesV_1356	edgesV_1357	edgesV_1358	edgesV_1359	edgesV_1360	edgesV_1361	edgesV_1362	edgesV_1363	edgesV_1364	edgesV_1365	edgesV_1366	edgesV_1367	edgesV_1368	edgesV_1369	edgesV_1370	edgesV_1371	edgesV_1372	edgesV_1373	edgesV_1374	edgesV_1375	edgesV_1376	edgesV_1377	edgesV_1378	edgesV_1379	edgesV_1380	edgesV_1381	edgesV_1382	edgesV_1383	edgesV_1384	edgesV_1385	edgesV_1386	edgesV_1387	edgesV_1388	edgesV_1389	edgesV_1390	edgesV_1391	edgesV_1392	edgesV_1393	edgesV_1394	edgesV_1395	edgesV_1396	edgesV_1397	edgesV_1398	edgesV_1399	edgesV_1400	edgesV_1401	edgesV_1402	edgesV_1403	edgesV_1404	edgesV_1405	edgesV_1406	edgesV_1407	edgesV_1408	edgesV_1409	edgesV_1410	edgesV_1411	edgesV_1412	edgesV_1413	edgesV_1414	edgesV_1415	edgesV_1416	edgesV_1417	edgesV_1418	edgesV_1419	edgesV_1420	edgesV_1421	edgesV_1422	edgesV_1423	edgesV_1424	edgesV_1425	edgesV_1426	edgesV_1427	edgesV_1428	edgesV_1429	edgesV_1430	edgesV_1431	edgesV_1432	edgesV_1433	edgesV_1434	edgesV_1435	edgesV_1436	edgesV_1437	edgesV_1438	edgesV_1439	edgesV_1440	edgesV_1441	edgesV_1442	edgesV_1443	edgesV_1444	edgesV_1445	edgesV_1446	edgesV_1447	edgesV_1448	edgesV_1449	edgesV_1450	edgesV_1451	edgesV_1452	edgesV_1453	edgesV_1454	edgesV_1455	edgesV_1456	edgesV_1457	edgesV_1458	edgesV_1459	edgesV_1460	edgesV_1461	edgesV_1462	edgesV_1463	edgesV_1464	edgesV_1465	edgesV_1466	edgesV_1467	edgesV_1468	edgesV_1469	edgesV_1470	edgesV_1471	edgesV_1472	edgesV_1473	edgesV_1474	edgesV_1475	edgesV_1476	edgesV_1477	edgesV_1478	edgesV_1479	edgesV_1480	edgesV_1481	edgesV_1482	edgesV_1483	edgesV_1484	edgesV_1485	edgesV_1486	edgesV_1487	edgesV_1488	edgesV_1489	edgesV_1490	edgesV_1491	edgesV_1492	edgesV_1493	edgesV_1494	edgesV_1495	edgesV_1496	edgesV_1497	edgesV_1498	edgesV_1499	edgesV_1500	edgesV_1501	edgesV_1502	edgesV_1503	edgesV_1504	edgesV_1505	edgesV_1506	edgesV_1507	edgesV_1508	edgesV_1509	edgesV_1510	edgesV_1511	edgesV_1512	edgesV_1513	edgesV_1514	edgesV_1515	edgesV_1516	edgesV_1517	edgesV_1518	edgesV_1519	edgesV_1520	edgesV_1521	edgesV_1522	edgesV_1523	edgesV_1524	edgesV_1525	edgesV_1526	edgesV_1527	edgesV_1528	edgesV_1529	edgesV_1530	edgesV_1531	edgesV_1532	edgesV_1533	edgesV_1534	edgesV_1535	edgesV_1536	edgesV_1537	edgesV_1538	edgesV_1539	edgesV_1540	edgesV_1541	edgesV_1542	edgesV_1543	edgesV_1544	edgesV_1545	edgesV_1546	edgesV_1547	edgesV_1548	edgesV_1549	edgesV_1550	edgesV_1551	edgesV_1552	edgesV_1553	edgesV_1554	edgesV_1555	edgesV_1556	edgesV_1557	edgesV_1558	edgesV_1559	edgesV_1560	edgesV_1561	edgesV_1562	edgesV_1563	edgesV_1564	edgesV_1565	edgesV_1566	edgesV_1567	edgesV_1568	edgesV_1569	edgesV_1570	edgesV_1571	edgesV_1572	edgesV_1573	edgesV_1574	edgesV_1575	edgesV_1576	edgesV_1577	edgesV_1578	edgesV_1579	edgesV_1580	edgesV_1581	edgesV_1582	edgesV_1583	edgesV_1584	edgesV_1585	edgesV_1586	edgesV_1587	edgesV_1588	edgesV_1589	edgesV_1590	edgesV_1591	edgesV_1592	edgesV_1593	edgesV_1594	edgesV_1595	edgesV_1596	edgesV_1597	edgesV_1598	edgesV_1599	edgesV_1600	edgesV_1601	edgesV_1602	edgesV_1603	edgesV_1604	edgesV_1605	edgesV_1606	edgesV_1607	edgesV_1608	edgesV_1609	edgesV_1610	edgesV_1611	edgesV_1612	edgesV_1613	edgesV_1614	edgesV_1615	edgesV_1616	edgesV_1617	edgesV_1618	edgesV_1619	edgesV_1620	edgesV_1621	edgesV_1622	edgesV_1623	edgesV_1624	edgesV_1625	edgesV_1626	edgesV_1627	edgesV_1628	edgesV_1629	edgesV_1630	edgesV_1631	edgesV_1632	edgesV_1633	edgesV_1634	edgesV_1635	edgesV_1636	edgesV_1637	edgesV_1638	edgesV_1639	edgesV_1640	edgesV_1641	edgesV_1642	edgesV_1643	edgesV_1644	edgesV_1645	edgesV_1646	edgesV_1647	edgesV_1648	edgesV_1649	edgesV_1650	edgesV_1651	edgesV_1652	edgesV_1653	edgesV_1654	edgesV_1655	edgesV_1656	edgesV_1657	edgesV_1658	edgesV_1659	edgesV_1660	edgesV_1661	edgesV_1662	edgesV_1663	edgesV_1664	edgesV_1665	edgesV_1666	edgesV_1667	edgesV_1668	edgesV_1669	edgesV_1670	edgesV_1671	edgesV_1672	edgesV_1673	edgesV_1674	edgesV_1675	edgesV_1676	edgesV_1677	edgesV_1678	edgesV_1679	edgesV_1680	edgesV_1681	edgesV_1682	edgesV_1683	edgesV_1684	edgesV_1685	edgesV_1686	edgesV_1687	edgesV_1688	edgesV_1689	edgesV_1690	edgesV_1691	edgesV_1692	edgesV_1693	edgesV_1694	edgesV_1695	edgesV_1696	edgesV_1697	edgesV_1698	edgesV_1699	edgesV_1700	edgesV_1701	edgesV_1702	edgesV_1703	edgesV_1704	edgesV_1705	edgesV_1706	edgesV_1707	edgesV_1708	edgesV_1709	edgesV_1710	edgesV_1711	edgesV_1712	edgesV_1713	edgesV_1714	edgesV_1715	edgesV_1716	edgesV_1717	edgesV_1718	edgesV_1719	edgesV_1720	edgesV_1721	edgesV_1722	edgesV_1723	edgesV_1724	edgesV_1725	edgesV_1726	edgesV_1727	edgesV_1728	edgesV_1729	edgesV_1730	edgesV_1731	edgesV_1732	edgesV_1733	edgesV_1734	edgesV_1735	edgesV_1736	edgesV_1737	edgesV_1738	edgesV_1739	edgesV_1740	edgesV_1741	edgesV_1742	edgesV_1743	edgesV_1744	edgesV_1745	edgesV_1746	edgesV_1747	edgesV_1748	edgesV_1749	edgesV_1750	edgesV_1751	edgesV_1752	edgesV_1753	edgesV_1754	edgesV_1755	edgesV_1756	edgesV_1757	edgesV_1758	edgesV_1759	edgesV_1760	edgesV_1761	edgesV_1762	edgesV_1763	edgesV_1764	edgesV_1765	edgesV_1766	edgesV_1767	edgesV_1768	edgesV_1769	edgesV_1770	edgesV_1771	edgesV_1772	edgesV_1773	edgesV_1774	edgesV_1775	edgesV_1776	edgesV_1777	edgesV_1778	edgesV_1779	edgesV_1780	edgesV_1781	edgesV_1782	edgesV_1783	edgesV_1784	edgesV_1785	edgesV_1786	edgesV_1787	edgesV_1788	edgesV_1789	edgesV_1790	edgesV_1791	edgesV_1792	edgesV_1793	edgesV_1794	edgesV_1795	edgesV_1796	edgesV_1797	edgesV_1798	edgesV_1799	edgesV_1800	edgesV_1801	edgesV_1802	edgesV_1803	edgesV_1804	edgesV_1805	edgesV_1806	edgesV_1807	edgesV_1808	edgesV_1809	edgesV_1810	edgesV_1811	edgesV_1812	edgesV_1813	edgesV_1814	edgesV_1815	edgesV_1816	edgesV_1817	edgesV_1818	edgesV_1819	edgesV_1820	edgesV_1821	edgesV_1822	edgesV_1823	edgesV_1824	edgesV_1825	edgesV_1826	edgesV_1827	edgesV_1828	edgesV_1829	edgesV_1830	edgesV_1831	edgesV_1832	edgesV_1833	edgesV_1834	edgesV_1835	edgesV_1836	edgesV_1837	edgesV_1838	edgesV_1839	edgesV_1840	edgesV_1841	edgesV_1842	edgesV_1843	edgesV_1844	edgesV_1845	edgesV_1846	edgesV_1847	edgesV_1848	edgesV_1849	edgesV_1850	edgesV_1851	edgesV_1852	edgesV_1853	edgesV_1854	edgesV_1855	edgesV_1856	edgesV_1857	edgesV_1858	edgesV_1859	edgesV_1860	edgesV_1861	edgesV_1862	edgesV_1863	edgesV_1864	edgesV_1865	edgesV_1866	edgesV_1867	edgesV_1868	edgesV_1869	edgesV_1870	edgesV_1871	edgesV_1872	edgesV_1873	edgesV_1874	edgesV_1875	edgesV_1876	edgesV_1877	edgesV_1878	edgesV_1879	edgesV_1880	edgesV_1881	edgesV_1882	edgesV_1883	edgesV_1884	edgesV_1885	edgesV_1886	edgesV_1887	edgesV_1888	edgesV_1889	edgesV_1890	edgesV_1891	edgesV_1892	edgesV_1893	edgesV_1894	edgesV_1895	edgesV_1896	edgesV_1897	edgesV_1898	edgesV_1899	edgesV_1900	edgesV_1901	edgesV_1902	edgesV_1903	edgesV_1904	edgesV_1905	edgesV_1906	edgesV_1907	edgesV_1908	edgesV_1909	edgesV_1910	edgesV_1911	edgesV_1912	edgesV_1913	edgesV_1914	edgesV_1915	edgesV_1916	edgesV_1917	edgesV_1918	edgesV_1919	edgesV_1920	edgesV_1921	edgesV_1922	edgesV_1923	edgesV_1924	edgesV_1925	edgesV_1926	edgesV_1927	edgesV_1928	edgesV_1929	edgesV_1930	edgesV_1931	edgesV_1932	edgesV_1933	edgesV_1934	edgesV_1935	edgesV_1936	edgesV_1937	edgesV_1938	edgesV_1939	edgesV_1940	edgesV_1941	edgesV_1942	edgesV_1943	edgesV_1944	edgesV_1945	edgesV_1946	edgesV_1947	edgesV_1948	edgesV_1949	edgesV_1950	edgesV_1951	edgesV_1952	edgesV_1953	edgesV_1954	edgesV_1955	edgesV_1956	edgesV_1957	edgesV_1958	edgesV_1959	edgesV_1960	edgesV_1961	edgesV_1962	edgesV_1963	edgesV_1964	edgesV_1965	edgesV_1966	edgesV_1967	edgesV_1968	edgesV_1969	edgesV_1970	edgesV_1971	edgesV_1972	edgesV_1973	edgesV_1974	edgesV_1975	edgesV_1976	edgesV_1977	edgesV_1978	edgesV_1979	edgesV_1980	edgesV_1981	edgesV_1982	edgesV_1983	edgesV_1984	edgesV_1985	edgesV_1986	edgesV_1987	edgesV_1988	edgesV_1989	edgesV_1990	edgesV_1991	edgesV_1992	edgesV_1993	edgesV_1994	edgesV_1995	edgesV_1996	edgesV_1997	edgesV_1998	edgesV_1999	edgesV_2000	edgesV_2001	edgesV_2002	edgesV_2003	edgesV_2004	edgesV_2005	edgesV_2006	edgesV_2007	edgesV_2008	edgesV_2009	edgesV_2010	edgesV_2011	edgesV_2012	edgesV_2013	edgesV_2014	edgesV_2015	edgesV_2016	edgesV_2017	edgesV_2018	edgesV_2019	edgesV_2020	edgesV_2021	edgesV_2022	edgesV_2023	edgesV_2024	edgesV_2025	edgesV_2026	edgesV_2027	edgesV_2028	edgesV_2029	edgesV_2030	edgesV_2031	edgesV_2032	edgesV_2033	edgesV_2034	edgesV_2035	edgesV_2036	edgesV_2037	edgesV_2038	edgesV_2039	edgesV_2040	edgesV_2041	edgesV_2042	edgesV_2043	edgesV_2044	edgesV_2045	edgesV_2046	edgesV_2047	edgesV_2048
#0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99	100	101	102	103	104	105	106	107	108	109	110	111	112	113	114	115	116	117	118	119	120	121	122	123	124	125	126	127	128	129	130	131	132	133	134	135	136	137	138	139	140	141	142	143	144	145	146	147	148	149	150	151	152	153	154	155	156	157	158	159	160	161	162	163	164	165	166	167	168	169	170	171	172	173	174	175	176	177	178	179	180	181	182	183	184	185	186	187	188	189	190	191	192	193	194	195	196	197	198	199	200	201	202	203	204	205	206	207	208	209	210	211	212	213	214	215	216	217	218	219	220	221	222	223	224	225	226	227	228	229	230	231	232	233	234	235	236	237	238	239	240	241	242	243	244	245	246	247	248	249	250	251	252	253	254	255	256	257	258	259	260	261	262	263	264	265	266	267	268	269	270	271	272	273	274	275	276	277	278	279	280	281	282	283	284	285	286	287	288	289	290	291	292	293	294	295	296	297	298	299	300	301	302	303	304	305	306	307	308	309	310	311	312	313	314	315	316	317	318	319	320	321	322	323	324	325	326	327	328	329	330	331	332	333	334	335	336	337	338	339	340	341	342	343	344	345	346	347	348	349	350	351	352	353	354	355	356	357	358	359	360	361	362	363	364	365	366	367	368	369	370	371	372	373	374	375	376	377	378	379	380	381	382	383	384	385	386	387	388	389	390	391	392	393	394	395	396	397	398	399	400	401	402	403	404	405	406	407	408	409	410	411	412	413	414	415	416	417	418	419	420	421	422	423	424	425	426	427	428	429	430	431	432	433	434	435	436	437	438	439	440	441	442	443	444	445	446	447	448	449	450	451	452	453	454	455	456	457	458	459	460	461	462	463	464	465	466	467	468	469	470	471	472	473	474	475	476	477	478	479	480	481	482	483	484	485	486	487	488	489	490	491	492	493	494	495	496	497	498	499	500	501	502	503	504	505	506	507	508	509	510	511	512	513	514	515	516	517	518	519	520	521	522	523	524	525	526	527	528	529	530	531	532	533	534	535	536	537	538	539	540	541	542	543	544	545	546	547	548	549	550	551	552	553	554	555	556	557	558	559	560	561	562	563	564	565	566	567	568	569	570	571	572	573	574	575	576	577	578	579	580	581	582	583	584	585	586	587	588	589	590	591	592	593	594	595	596	597	598	599	600	601	602	603	604	605	606	607	608	609	610	611	612	613	614	615	616	617	618	619	620	621	622	623	624	625	626	627	628	629	630	631	632	633	634	635	636	637	638	639	640	641	642	643	644	645	646	647	648	649	650	651	652	653	654	655	656	657	658	659	660	661	662	663	664	665	666	667	668	669	670	671	672	673	674	675	676	677	678	679	680	681	682	683	684	685	686	687	688	689	690	691	692	693	694	695	696	697	698	699	700	701	702	703	704	705	706	707	708	709	710	711	712	713	714	715	716	717	718	719	720	721	722	723	724	725	726	727	728	729	730	731	732	733	734	735	736	737	738	739	740	741	742	743	744	745	746	747	748	749	750	751	752	753	754	755	756	757	758	759	760	761	762	763	764	765	766	767	768	769	770	771	772	773	774	775	776	777	778	779	780	781	782	783	784	785	786	787	788	789	790	791	792	793	794	795	796	797	798	799	800	801	802	803	804	805	806	807	808	809	810	811	812	813	814	815	816	817	818	819	820	821	822	823	824	825	826	827	828	829	830	831	832	833	834	835	836	837	838	839	840	841	842	843	844	845	846	847	848	849	850	851	852	853	854	855	856	857	858	859	860	861	862	863	864	865	866	867	868	869	870	871	872	873	874	875	876	877	878	879	880	881	882	883	884	885	886	887	888	889	890	891	892	893	894	895	896	897	898	899	900	901	902	903	904	905	906	907	908	909	910	911	912	913	914	915	916	917	918	919	920	921	922	923	924	925	926	927	928	929	930	931	932	933	934	935	936	937	938	939	940	941	942	943	944	945	946	947	948	949	950	951	952	953	954	955	956	957	958	959	960	961	962	963	964	965	966	967	968	969	970	971	972	973	974	975	976	977	978	979	980	981	982	983	984	985	986	987	988	989	990	991	992	993	994	995	996	997	998	999	1000	1001	1002	1003	1004	1005	1006	1007	1008	1009	1010	1011	1012	1013	1014	1015	1016	1017	1018	1019	1020	1021	1022	1023	1024	1025	1026	1027	1028	1029	1030	1031	1032	1033	1034	1035	1036	1037	1038	1039	1040	1041	1042	1043	1044	1045	1046	1047	1048	1049	1050	1051	1052	1053	1054	1055	1056	1057	1058	1059	1060	1061	1062	1063	1064	1065	1066	1067	1068	1069	1070	1071	1072	1073	1074	1075	1076	1077	1078	1079	1080	1081	1082	1083	1084	1085	1086	1087	1088	1089	1090	1091	1092	1093	1094	1095	1096	1097	1098	1099	1100	1101	1102	1103	1104	1105	1106	1107	1108	1109	1110	1111	1112	1113	1114	1115	1116	1117	1118	1119	1120	1121	1122	1123	1124	1125	1126	1127	1128	1129	1130	1131	1132	1133	1134	1135	1136	1137	1138	1139	1140	1141	1142	1143	1144	1145	1146	1147	1148	1149	1150	1151	1152	1153	1154	1155	1156	1157	1158	1159	1160	1161	1162	1163	1164	1165	1166	1167	1168	1169	1170	1171	1172	1173	1174	1175	1176	1177	1178	1179	1180	1181	1182	1183	1184	1185	1186	1187	1188	1189	1190	1191	1192	1193	1194	1195	1196	1197	1198	1199	1200	1201	1202	1203	1204	1205	1206	1207	1208	1209	1210	1211	1212	1213	1214	1215	1216	1217	1218	1219	1220	1221	1222	1223	1224	1225	1226	1227	1228	1229	1230	1231	1232	1233	1234	1235	1236	1237	1238	1239	1240	1241	1242	1243	1244	1245	1246	1247	1248	1249	1250	1251	1252	1253	1254	1255	1256	1257	1258	1259	1260	1261	1262	1263	1264	1265	1266	1267	1268	1269	1270	1271	1272	1273	1274	1275	1276	1277	1278	1279	1280	1281	1282	1283	1284	1285	1286	1287	1288	1289	1290	1291	1292	1293	1294	1295	1296	1297	1298	1299	1300	1301	1302	1303	1304	1305	1306	1307	1308	1309	1310	1311	1312	1313	1314	1315	1316	1317	1318	1319	1320	1321	1322	1323	1324	1325	1326	1327	1328	1329	1330	1331	1332	1333	1334	1335	1336	1337	1338	1339	1340	1341	1342	1343	1344	1345	1346	1347	1348	1349	1350	1351	1352	1353	1354	1355	1356	1357	1358	1359	1360	1361	1362	1363	1364	1365	1366	1367	1368	1369	1370	1371	1372	1373	1374	1375	1376	1377	1378	1379	1380	1381	1382	1383	1384	1385	1386	1387	1388	1389	1390	1391	1392	1393	1394	1395	1396	1397	1398	1399	1400	1401	1402	1403	1404	1405	1406	1407	1408	1409	1410	1411	1412	1413	1414	1415	1416	1417	1418	1419	1420	1421	1422	1423	1424	1425	1426	1427	1428	1429	1430	1431	1432	1433	1434	1435	1436	1437	1438	1439	1440	1441	1442	1443	1444	1445	1446	1447	1448	1449	1450	1451	1452	1453	1454	1455	1456	1457	1458	1459	1460	1461	1462	1463	1464	1465	1466	1467	1468	1469	1470	1471	1472	1473	1474	1475	1476	1477	1478	1479	1480	1481	1482	1483	1484	1485	1486	1487	1488	1489	1490	1491	1492	1493	1494	1495	1496	1497	1498	1499	1500	1501	1502	1503	1504	1505	1506	1507	1508	1509	1510	1511	1512	1513	1514	1515	1516	1517	1518	1519	1520	1521	1522	1523	1524	1525	1526	1527	1528	1529	1530	1531	1532	1533	1534	1535	1536	1537	1538	1539	1540	1541	1542	1543	1544	1545	1546	1547	1548	1549	1550	1551	1552	1553	1554	1555	1556	1557	1558	1559	1560	1561	1562	1563	1564	1565	1566	1567	1568	1569	1570	1571	1572	1573	1574	1575	1576	1577	1578	1579	1580	1581	1582	1583	1584	1585	1586	1587	1588	1589	1590	1591	1592	1593	1594	1595	1596	1597	1598	1599	1600	1601	1602	1603	1604	1605	1606	1607	1608	1609	1610	1611	1612	1613	1614	1615	1616	1617	1618	1619	1620	1621	1622	1623	1624	1625	1626	1627	1628	1629	1630	1631	1632	1633	1634	1635	1636	1637	1638	1639	1640	1641	1642	1643	1644	1645	1646	1647	1648	1649	1650	1651	1652	1653	1654	1655	1656	1657	1658	1659	1660	1661	1662	1663	1664	1665	1666	1667	1668	1669	1670	1671	1672	1673	1674	1675	1676	1677	1678	1679	1680	1681	1682	1683	1684	1685	1686	1687	1688	1689	1690	1691	1692	1693	1694	1695	1696	1697	1698	1699	1700	1701	1702	1703	1704	1705	1706	1707	1708	1709	1710	1711	1712	1713	1714	1715	1716	1717	1718	1719	1720	1721	1722	1723	1724	1725	1726	1727	1728	1729	1730	1731	1732	1733	1734	1735	1736	1737	1738	1739	1740	1741	1742	1743	1744	1745	1746	1747	1748	1749	1750	1751	1752	1753	1754	1755	1756	1757	1758	1759	1760	1761	1762	1763	1764	1765	1766	1767	1768	1769	1770	1771	1772	1773	1774	1775	1776	1777	1778	1779	1780	1781	1782	1783	1784	1785	1786	1787	1788	1789	1790	1791	1792	1793	1794	1795	1796	1797	1798	1799	1800	1801	1802	1803	1804	1805	1806	1807	1808	1809	1810	1811	1812	1813	1814	1815	1816	1817	1818	1819	1820	1821	1822	1823	1824	1825	1826	1827	1828	1829	1830	1831	1832	1833	1834	1835	1836	1837	1838	1839	1840	1841	1842	1843	1844	1845	1846	1847	1848	1849	1850	1851	1852	1853	1854	1855	1856	1857	1858	1859	1860	1861	1862	1863	1864	1865	1866	1867	1868	1869	1870	1871	1872	1873	1874	1875	1876	1877	1878	1879	1880	1881	1882	1883	1884	1885	1886	1887	1888	1889	1890	1891	1892	1893	1894	1895	1896	1897	1898	1899	1900	1901	1902	1903	1904	1905	1906	1907	1908	1909	1910	1911	1912	1913	1914	1915	1916	1917	1918	1919	1920	1921	1922	1923	1924	1925	1926	1927	1928	1929	1930	1931	1932	1933	1934	1935	1936	1937	1938	1939	1940	1941	1942	1943	1944	1945	1946	1947	1948	1949	1950	1951	1952	1953	1954	1955	1956	1957	1958	1959	1960	1961	1962	1963	1964	1965	1966	1967	1968	1969	1970	1971	1972	1973	1974	1975	1976	1977	1978	1979	1980	1981	1982	1983	1984	1985	1986	1987	1988	1989	1990	1991	1992	1993	1994	1995	1996	1997	1998	1999	2000	2001	2002	2003	2004	2005	2006	2007	2008	2009	2010	2011	2012	2013	2014	2015	2016	2017	2018	2019	2020	2021	2022	2023	2024	2025	2026	2027	2028	2029	2030	2031	2032	2033	2034	2035	2036	2037	2038	2039	2040	2041	2042	2043	2044	2045	2046	2047	2048	2049	2050	2051	2052	2053	2054	2055	2056	2057	2058	2059	2060	2061	2062	2063	2064
COL_AccessionNumber = 0
COL_isDecentArtists = 1
COL_artworksLG5 = 2
COL_artworksLG10 = 3
COL_HueArithmeticAverage = 4
COL_Entropy = 14
COL_hasKaze = 15
COL_edgesV_1 = 17
batchSz = 100

FFNN_train_avg_acc = []
FFNN_test_avg_acc = []
FFNN_precision_avg = []
FFNN_recall_avg = []
FFNN_FOne_avg = []
FFNN_ROC_AUC_avg = []
FFNN_log_loss_avg = []

SVM_train_avg_acc = []
SVM_test_avg_acc = []
SVM_loss_avg_acc = []
SVM_precision_avg = []
SVM_recall_avg = []
SVM_FOne_avg = []
SVM_ROC_AUC_avg = []
SVM_log_loss_avg = []

def msqrt(X):
    '''Computes the square root matrix of symmetric square matrix X.'''
    (L, V) = np.linalg.eig(X)
    return V.dot(np.diag(np.sqrt(L))).dot(V.T) 

def zca_whitening_matrix(X):
    """
    Function to compute ZCA whitening matrix (aka Mahalanobis whitening).
    INPUT:  X: [M x N] matrix.
        Rows: Variables
        Columns: Observations
    OUTPUT: ZCAMatrix: [M x M] matrix
    """
    # Covariance matrix [column-wise variables]: Sigma = (X-mu)' * (X-mu) / N
    sigma = np.cov(X, rowvar=True) # [M x M]
    # Singular Value Decomposition. X = U * np.diag(S) * V
    U,S,V = np.linalg.svd(sigma)
        # U: [M x M] eigenvectors of sigma.
        # S: [M x 1] eigenvalues of sigma.
        # V: [M x M] transpose of U
    # Whitening constant: prevents division by zero
    epsilon = 1e-5
    # ZCA Whitening matrix: U * Lambda * U'
    ZCAMatrix = np.dot(U, np.dot(np.diag(1.0/np.sqrt(S + epsilon)), U.T)) # [M x M]
    return np.dot(ZCAMatrix, X)

def tensorFFNN(featurefilename, outfile):
    # To open Workbook 
    wb = xlrd.open_workbook(momafilename) 
    sheet = wb.sheet_by_index(0)

# Kaze Feature extractor  
def kaze_extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path, 0)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        if dsc is None:
            ##print(image_path)
            return None
        else:
            dsc = dsc.flatten()
            # Making descriptor of same size
            # Descriptor vector size is 64
            needed_size = (vector_size * 64)
            if dsc.size < needed_size:
                # if we have less the 32 descriptors then just adding zeros at the
                # end of our feature vector
                dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: %s'% e)
        return None

    return dsc

def extractFeaturesbyGivenFile(feature_file, isLG10):
    
    # To open Workbook 
    wb = xlrd.open_workbook(feature_file) 
    sheet = wb.sheet_by_index(0)
    #sheet = pd.read_excel(feature_file, sheet_name='MoMAPaintingQArtLearnDecentArti')
    #matrix = sheet.as_matrix()
    
    featuresStatistic=[]
    featuresKaze=[]
    featuresAll=[]
    predictV=[]
    rows = 0
    for row in range (1, sheet.nrows):
        _rowStatistic = []
        _rowKaze = []
        _rowAll = []
        #hasKaze = int(sheet.cell_value(row, 4).split(',')[0])
        hasKaze = int(sheet.cell_value(row, COL_hasKaze))
        artworks2Count = int(sheet.cell_value(row,COL_artworksLG10)) if (isLG10==1) else int(sheet.cell_value(row,COL_artworksLG5))
        if (hasKaze == 1 and artworks2Count == 1):
            rows = rows + 1
            for col in range (sheet.ncols):
                if ((col >= COL_HueArithmeticAverage and col <= COL_Entropy) or (col >= COL_edgesV_1)):
                    cellVale = float(sheet.cell_value(row,col))
                  
                if (col >= COL_HueArithmeticAverage and col <= COL_Entropy):
                    #print('row: %d, col: %d, value: %s, len: %d' % (row, col, sheet.cell_value(row,col), len(sheet.cell_value(row,col))))
                    _rowStatistic.append(cellVale)
                    _rowAll.append(cellVale)
                elif (col >= COL_edgesV_1):
                    _rowKaze.append(cellVale)
                    _rowAll.append(cellVale)
                else:
                    continue
            
            featuresStatistic.append(_rowStatistic)
            featuresKaze.append(_rowKaze)
            featuresAll.append(_rowAll)
            predictV.append(int(sheet.cell_value(row,COL_isDecentArtists)))
            
    return featuresStatistic, featuresKaze, featuresAll, predictV, rows, len(featuresStatistic[0]), len(featuresKaze[0]), len(featuresAll[0])

'''
    num_cols = sheet#sheet.ncols   # Number of columns
    num_rows = sheet.nrows - 1
    if (isLG10 == 1):
        featuresM = sheet.col_values(4, sheet.ncols)[sheet.col_values(3)==1]
        predictV = sheet.col_values(1)[sheet.col_values(3)==1]
    else:
        featuresM = sheet.col_values(4, sheet.ncols)[sheet.col_values(2)==1]
        predictV = sheet.col_values(1)[sheet.col_values(2)==1]
'''

def randomPartition(featuresW, predictV):
    anotherV = []
    for idx, val in enumerate(predictV):
        row=[]
        row.append(idx)
        row.append(val)
        anotherV.append(row)
    
    #anotherV.sort(key = anotherV[1])
    boolV = np.array(anotherV)[:,1]>0
    posV = np.array(anotherV)[boolV]
    boolV = np.array(anotherV)[:,1]==0
    negV = np.array(anotherV)[boolV]
    
    train_posV_indices = np.random.choice(len(posV), round(len(posV)*0.8), replace=False)
    train_posV_idx = np.array(posV)[train_posV_indices][:,0]
    test_posV_indices = np.array(list(set(range(len(posV))) - set(train_posV_indices)))
    test_posV_idx = np.array(posV)[test_posV_indices][:,0]
    train_negV_indices = np.random.choice(len(negV), round(len(negV)*0.8), replace=False)
    train_negV_idx = np.array(negV)[train_negV_indices][:,0]
    test_negV_indices = np.array(list(set(range(len(negV))) - set(train_negV_indices)))
    test_negV_idx = np.array(negV)[test_negV_indices][:,0]
        
    xtrain_pos = featuresW[train_posV_idx]
    xtrain_neg = featuresW[train_negV_idx]
    xtest_pos = featuresW[test_posV_idx]
    xtest_neg = featuresW[test_negV_idx]    
    
    ytrain_pos = np.array(predictV)[train_posV_idx]
    ytrain_neg = np.array(predictV)[train_negV_idx]
    ytest_pos = np.array(predictV)[test_posV_idx]
    ytest_neg = np.array(predictV)[test_negV_idx]
    
    train_indices = list(train_posV_idx) + list(train_negV_idx)
    test_indices = list(test_posV_idx) + list(test_negV_idx)

    xtrain = featuresW[train_indices]
    xtest = featuresW[test_indices]
    
    ytrain = np.array(predictV)[train_indices]
    ytest = np.array(predictV)[test_indices]

    return xtrain, xtest, ytrain, ytest, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg

    
# tensor FFNN images - sample testing
def tensorFFNNImages(images_path, isLG10=1, predictionType=1, vector_size=32):
    batchSz = 100
    
    if isLG10 == 1:
        print('tensorFFNNImages on artworks which artists have more than ten painting pieces (and valid kaze features)')
    else:
        print('tensorFFNNImages on artworks which artists have more than five painting pieces (and valid kaze features)')
      
    # extract image features
    featuresStatistic, featuresKaze, featuresAll, predictV, rowsW, colsStatistic, colsKaze, colsAll = extractFeaturesbyGivenFile(images_path, isLG10) 
    if predictionType == 1:
        print('Feature selection is based on statistics.')
        featuresW = featuresStatistic
        colsW = colsStatistic
    elif predictionType == 2:
        print('Feature selection is based on kaze.')
        featuresW = featuresKaze
        colsW = colsKaze
    else:
        print('Feature selection is based on all.')
        featuresW = featuresAll
        colsW = colsAll
        
    # mimic prediction
    #y_anss = np.random.random(rowsW)
    #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
    anss = predictV

    print('#1 Declare variables')
    W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW))
    B = tf.Variable(tf.random.normal ([1], stddev = .1))
    
    print('#2 Decalre placeholder')
    img = tf.compat.v1.placeholder(tf.float32, [batchSz, colsW])
    ans = tf.compat.v1.placeholder(tf.float32, [batchSz])
    
    print('#3' )
    prbs = tf.nn.softmax(tf.matmul(img, W) + B)
    xEnt = tf.reduce_mean(-tf.reduce_sum(ans * tf.math.log(prbs), reduction_indices =[1]))
    
    print('#4')
    train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(xEnt)
    numCorrect = tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans))
    accuracy = tf.reduce_mean(tf.cast(numCorrect, tf.float32))

    print('#5')
    sess = tf.compat.v1.Session()
    sess.run(tf.global_variables_initializer())
    
    sumacc = 0
    for i in range(int(rowsW/batchSz)):
        indexL = i * batchSz
        indexH = (i+1) * batchSz  if rowsW >=(i+1) * batchSz else rowsW
        #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
        imgnp = featuresW[indexL:indexH]
        tanss = np.transpose(anss[indexL:indexH])
        sess.run(train, feed_dict={img: imgnp, ans: tanss})
        acc = sess.run(accuracy, feed_dict={img: imgnp, ans: tanss})
        print("Train Accuracy: %d %r" % (i, acc))
        sumacc += acc
    print("Train Accuracy:%r" % (sumacc/int(rowsW/batchSz)))
    #sumAcc = 0
    #sumAcc+= sess.run(accuracy, feed_dict={img: img, ans: ans})

def printPredictionMeasure(timesMax, preTrainBagMax, isLG10, predictionType):
    print('timesMax=%d, preTrainBagMax=%d' % (timesMax, preTrainBagMax))
    print('FFNN Images Bagging Pre-training isLG10=%d predictionType=%d times' % (isLG10, predictionType))
    print("Average Train Accuracy:%r" % (np.average(FFNN_train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(FFNN_test_avg_acc)))
    print("Precision:%r" % (np.average(FFNN_precision_avg)))
    print("Recall:%r" % (np.average(FFNN_recall_avg)))
    print("F1:%r" % (np.average(FFNN_FOne_avg)))
    print("Log loss:%r" % (np.average(FFNN_log_loss_avg)))
    
    print('SVM Images Bagging Pre-training isLG10=%d predictionType=%d times' % (isLG10, predictionType))
    print("Average Train Accuracy:%r" % (np.average(SVM_train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(SVM_test_avg_acc)))
    print("Precision:%r" % (np.average(SVM_precision_avg)))
    print("Recall:%r" % (np.average(SVM_recall_avg)))
    print("F1:%r" % (np.average(SVM_FOne_avg)))
    print("Log loss:%r" % (np.average(SVM_log_loss_avg)))    
    
def tensorFFNNImagesBaggingLearning(colsW, preTrainBagMax, x_vals_train, x_vals_test, y_vals_train, y_vals_test, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg):
    #print('#1 Declare variables')
    W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW))
    B = tf.Variable(tf.random.normal ([1], stddev = .1))
    
    #print('#2 Decalre placeholder')
    img = tf.compat.v1.placeholder(tf.float32, [None, colsW])
    ans = tf.compat.v1.placeholder(tf.float32, [None,1])
    
    #print('#3 Calculate cross-entropy' )
    prbs = tf.nn.softmax(tf.matmul(img, W) + B)
    xEnt = tf.reduce_mean(-tf.reduce_sum(ans * tf.math.log(prbs), reduction_indices =[1]))
    
    #print('#4 Prediction measurement')
    train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(xEnt)
    numCorrect = tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans))
    accuracy = tf.reduce_mean(tf.cast(numCorrect, tf.float32))
    predicted = tf.multiply(tf.cast(tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans)), tf.float32), ans)
    
    TP = tf.count_nonzero(tf.multiply(predicted, ans))
    TN = tf.count_nonzero(tf.multiply((predicted - 1), (ans - 1)))
    FP = tf.count_nonzero(tf.multiply(predicted, (ans - 1)))
    FN = tf.count_nonzero(tf.multiply((predicted - 1), ans))
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 * precision * recall / (precision + recall)
    log_loss = -tf.math.log((TP+TN) / (TP+TN+FP+FN))
    #roc_auc = sklearn.metrics.roc_auc_score(ans, tf.cast(tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans)), tf.float32))
    #roc_auc = tf.metrics.auc(ans,prbs, num_thresholds=50)
    
    #print('#5' )
    sess = tf.compat.v1.Session()
    sess.run(tf.compat.v1.global_variables_initializer())
    
    train_accuracy = []
    test_accuracy = []
    precision_list = []
    recall_list = []
    F1_list = []
    ROC_AUC_list = []
    log_loss_list = []
    for i in range(preTrainBagMax):
        rand_index = np.random.choice(len(x_vals_train), size=batchSz)
        X = x_vals_train[rand_index]
        Y = np.transpose([y_vals_train[rand_index]])

        #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
        imgnp = X
        tanss = Y
        sess.run(train, feed_dict={img: imgnp, ans: tanss})            
        train_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_train, ans: np.transpose([y_vals_train])})
        train_accuracy.append(train_acc_temp)
        test_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        test_accuracy.append(test_acc_temp)
        precision_temp = sess.run(precision, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        precision_list.append(precision_temp)
        recall_temp = sess.run(recall, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        recall_list.append(precision_temp)
        F1_temp = sess.run(f1, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        F1_list.append(F1_temp)
        log_loss_temp = sess.run(log_loss, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        log_loss_list.append(log_loss_temp)
        TP_temp = sess.run(TP, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        TN_temp = sess.run(TN, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        FP_temp = sess.run(FP, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        FN_temp = sess.run(FN, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        #AUC_temp = sess.run(roc_auc, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        if i % 300 == 0:
            print('FFNN Times: %d TP=%d, TN=%d, FP=%d, FN=%d' % (i, TP_temp, TN_temp, FP_temp, FN_temp))
    #print("Times: %d Train Accuracy:%r" % (times, np.average(train_accuracy)))
    #print("Times: %d Test Accuracy:%r" % (times, np.average(test_accuracy)))
    FFNN_train_avg_acc.append(np.average(train_accuracy))
    FFNN_test_avg_acc.append(np.average(test_accuracy))
    FFNN_precision_avg.append(np.average(precision_list))
    FFNN_recall_avg.append(np.average(recall_list))
    FFNN_FOne_avg.append(np.average(F1_list))
    FFNN_log_loss_avg.append(np.average(log_loss_list))
    
def tensorSVMImagesBagging(colsW, preTrainBagMax, x_vals_train, x_vals_test, y_vals_train, y_vals_test, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg):
    #print('#1 Declare variables')
    W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW)) #A
    B = tf.Variable(tf.random.normal ([1], stddev = .1))                                       #b
    
    #print('#2 Decalre placeholder')
    img = tf.compat.v1.placeholder(tf.float32, [None, colsW]) #x_data
    ans = tf.compat.v1.placeholder(tf.float32, [None, 1]) #y_target
    
    #Declare the model output.
    model_output = tf.subtract(tf.matmul(img, W), B) #x_data, A), b)
    #Declare the necessary components for the maximum margin loss.
    l2_norm = tf.reduce_sum(tf.square(W))
    alpha = tf.constant([0.1])
    classification_term = tf.reduce_mean(tf.maximum(0., tf.subtract(1.,tf.multiply(model_output, ans))))
    loss = tf.add(classification_term, tf.multiply(alpha, l2_norm))
    
    #Declare the prediction and accuracy functions.
    prediction = tf.sign(model_output)
    accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, ans),tf.float32))
    
    TP = tf.count_nonzero(tf.multiply(prediction, ans))
    TN = tf.count_nonzero(tf.multiply((prediction - 1), (ans - 1)))
    FP = tf.count_nonzero(tf.multiply(prediction, (ans - 1)))
    FN = tf.count_nonzero(tf.multiply((prediction - 1), ans))
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 * precision * recall / (precision + recall)
    log_loss = -tf.math.log((TP+TN) / (TP+TN+FP+FN))
    
    #Declare the optimizer.
    my_opt = tf.compat.v1.train.GradientDescentOptimizer(0.01)
    train = my_opt.minimize(loss)
    init = tf.compat.v1.global_variables_initializer()
    sess = tf.compat.v1.Session()
    sess.run(tf.compat.v1.global_variables_initializer())

    sumacc = 0
    loss_vec = []
    train_accuracy = []
    test_accuracy = []
    precision_list = []
    recall_list = []
    F1_list = []
    ROC_AUC_list = []
    log_loss_list = []
        #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
        imgnp = X
        tanss = Y
        sess.run(train, feed_dict={img: imgnp, ans: tanss})
        #acc = sess.run(accuracy, feed_dict={img: imgnp, ans: tanss})
        temp_loss = sess.run(loss, feed_dict={img: imgnp, ans: tanss})
        #loss_vec.append(temp_loss)
        train_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_train, ans: np.transpose([y_vals_train])})
        #train_accuracy.append(train_acc_temp)
        test_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        #test_accuracy.append(test_acc_temp)
        
        precision_temp = sess.run(precision, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        #precision_list.append(precision_temp)
        recall_temp = sess.run(recall, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        #recall_list.append(precision_temp)
        F1_temp = sess.run(f1, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        #F1_list.append(F1_temp)
        log_loss_temp = sess.run(log_loss, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        #log_loss_list.append(log_loss_temp)
        TP_temp = sess.run(TP, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        TN_temp = sess.run(TN, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        FP_temp = sess.run(FP, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        FN_temp = sess.run(FN, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        #AUC_temp = sess.run(roc_auc, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
        if i % 300 == 0:
            print('SVM Times: %d TP=%d, TN=%d, FP=%d, FN=%d' % (i, TP_temp, TN_temp, FP_temp, FN_temp))
    #print("Times: %d Train Accuracy:%r" % (times, np.average(train_accuracy)))
    #print("Times: %d Train Accuracy:%r" % (times, np.average(test_accuracy)))
    #print("Times: %d Loss :%r" % (times, np.average(loss_vec)))
    SVM_train_avg_acc.append(train_acc_temp) #np.average(train_accuracy))
    SVM_test_avg_acc.append(test_acc_temp)  #np.average(test_accuracy))
    SVM_loss_avg_acc.append(temp_loss)  #np.average(loss_vec))
    SVM_precision_avg.append(precision_temp) #np.average(precision_list))
    SVM_recall_avg.append(recall_temp) #np.average(recall_list))
    SVM_FOne_avg.append(F1_temp) #np.average(F1_list))
    SVM_log_loss_avg.append(np.average(log_loss_list))
    
def learningbyGivenFeatures(images_path, timesMax, preTrainBagMax, isLG10=1, predictionType=1, vector_size=32):
    batchSz = 100
    
    # extract image features
    #featuresW0, rowsW, colsW = extractFeaturesbyGivenFile(images_path) 
        
    if isLG10 == 1:
        print('tensorFFNNImagesBaggingPreTrainbyGivenFeatures on artworks which artists have more than ten painting pieces (and valid kaze features)')
    else:
        print('tensorFFNNImagesBaggingPreTrainbyGivenFeatures on artworks which artists have more than five painting pieces (and valid kaze features)')
      
    # extract image features
    featuresStatistic, featuresKaze, featuresAll, predictV, rowsW, colsStatistic, colsKaze, colsAll = extractFeaturesbyGivenFile(images_path, isLG10) 
    if predictionType == 1:
        print('Feature selection is based on statistics.')
        featuresW0 = featuresStatistic
        colsW = colsStatistic
    elif predictionType == 2:
        print('Feature selection is based on kaze.')
        featuresW0 = featuresKaze
        colsW = colsKaze
    else:
        print('Feature selection is based on all.')
        featuresW0 = featuresAll
        colsW = colsAll
        
    # mimic prediction
    #y_anss = np.random.random(rowsW)
    #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
    anss = predictV
    
    featuresW = zca_whitening_matrix(featuresW0)

    for times in range(timesMax):
        x_vals_train, x_vals_test, y_vals_train, y_vals_test, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg = randomPartition(featuresW, predictV)
        
        for i in range(preTrainBagMax):
            rand_index = np.random.choice(len(x_vals_train), size=batchSz)
            X = x_vals_train[rand_index]
            Y = np.transpose([y_vals_train[rand_index]])
    
            tensorFFNNImagesBaggingLearning(colsW, X, Y, preTrainBagMax, x_vals_train, x_vals_test, y_vals_train, y_vals_test, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg)
            tensorSVMImagesBagging(colsW, X, Y, preTrainBagMax, x_vals_train, x_vals_test, y_vals_train, y_vals_test, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg)
        
    printPredictionMeasure(timesMax, preTrainBagMax, isLG10, predictionType)
    


# outdated
def tensorFFNNImagesBaggingPreTrainbyGivenFeatures(images_path, timesMax, preTrainBagMax, isLG10=1, predictionType=1, vector_size=32):
    batchSz = 100
    
    # extract image features
    #featuresW0, rowsW, colsW = extractFeaturesbyGivenFile(images_path) 
        
    if isLG10 == 1:
        print('tensorFFNNImagesBaggingPreTrainbyGivenFeatures on artworks which artists have more than ten painting pieces (and valid kaze features)')
    else:
        print('tensorFFNNImagesBaggingPreTrainbyGivenFeatures on artworks which artists have more than five painting pieces (and valid kaze features)')
      
    # extract image features
    featuresStatistic, featuresKaze, featuresAll, predictV, rowsW, colsStatistic, colsKaze, colsAll = extractFeaturesbyGivenFile(images_path, isLG10) 
    if predictionType == 1:
        print('Feature selection is based on statistics.')
        featuresW0 = featuresStatistic
        colsW = colsStatistic
    elif predictionType == 2:
        print('Feature selection is based on kaze.')
        featuresW0 = featuresKaze
        colsW = colsKaze
    else:
        print('Feature selection is based on all.')
        featuresW0 = featuresAll
        colsW = colsAll
        
    # mimic prediction
    #y_anss = np.random.random(rowsW)
    #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
    anss = predictV
    
    featuresW = zca_whitening_matrix(featuresW0)
    train_avg_acc = []
    test_avg_acc = []
    precision_avg = []
    recall_avg = []
    FOne_avg = []
    ROC_AUC_avg = []
    log_loss_avg = []
    for times in range(timesMax):
        '''
        #Split the training data and testing data.
        train_indices = np.random.choice(len(featuresW), round(len(featuresW)*0.5), replace=False)
        test_indices = np.array(list(set(range(len(featuresW))) - set(train_indices)))
        x_vals_train = np.array(featuresW)[train_indices]
        x_vals_test = np.array(featuresW)[test_indices]
        
        # mimic prediction
        #y_anss = np.random.random(rowsW)
        #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
        
        y_vals_train = np.array(anss)[train_indices]
        y_vals_test = np.array(anss)[test_indices]
        '''
        
        x_vals_train, x_vals_test, y_vals_train, y_vals_test, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg = randomPartition(featuresW, predictV)

        #print('#1 Declare variables')
        W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW))
        B = tf.Variable(tf.random.normal ([1], stddev = .1))
        
        #print('#2 Decalre placeholder')
        img = tf.compat.v1.placeholder(tf.float32, [None, colsW])
        ans = tf.compat.v1.placeholder(tf.float32, [None,1])
        
        #print('#3 Calculate cross-entropy' )
        prbs = tf.nn.softmax(tf.matmul(img, W) + B)
        xEnt = tf.reduce_mean(-tf.reduce_sum(ans * tf.math.log(prbs), reduction_indices =[1]))
        
        #print('#4 Prediction measurement')
        train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(xEnt)
        numCorrect = tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans))
        accuracy = tf.reduce_mean(tf.cast(numCorrect, tf.float32))
        predicted = tf.multiply(tf.cast(tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans)), tf.float32), ans)
        
        TP = tf.count_nonzero(tf.multiply(predicted, ans))
        TN = tf.count_nonzero(tf.multiply((predicted - 1), (ans - 1)))
        FP = tf.count_nonzero(tf.multiply(predicted, (ans - 1)))
        FN = tf.count_nonzero(tf.multiply((predicted - 1), ans))
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        f1 = 2 * precision * recall / (precision + recall)
        log_loss = -tf.math.log((TP+TN) / (TP+TN+FP+FN))
        #roc_auc = sklearn.metrics.roc_auc_score(ans, tf.cast(tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans)), tf.float32))
        #roc_auc = tf.metrics.auc(ans,prbs, num_thresholds=50)
        
        #print('#5' )
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())
        
        train_accuracy = []
        test_accuracy = []
        precision_list = []
        recall_list = []
        F1_list = []
        ROC_AUC_list = []
        log_loss_list = []
        for i in range(preTrainBagMax):
            rand_index = np.random.choice(len(x_vals_train), size=batchSz)
            X = x_vals_train[rand_index]
            Y = np.transpose([y_vals_train[rand_index]])

            #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
            imgnp = X
            tanss = Y
            sess.run(train, feed_dict={img: imgnp, ans: tanss})            
            train_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_train, ans: np.transpose([y_vals_train])})
            train_accuracy.append(train_acc_temp)
            test_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            test_accuracy.append(test_acc_temp)
            precision_temp = sess.run(precision, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            precision_list.append(precision_temp)
            recall_temp = sess.run(recall, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            recall_list.append(precision_temp)
            F1_temp = sess.run(f1, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            F1_list.append(F1_temp)
            log_loss_temp = sess.run(log_loss, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            log_loss_list.append(log_loss_temp)
            TP_temp = sess.run(TP, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            TN_temp = sess.run(TN, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            FP_temp = sess.run(FP, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            FN_temp = sess.run(FN, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            AUC_temp = sess.run(roc_auc, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            print('Times: %d TP=%d, TN=%d, FP=%d, FN=%d' % (i, TP_temp, TN_temp, FP_temp, FN_temp))
        #print("Times: %d Train Accuracy:%r" % (times, np.average(train_accuracy)))
        #print("Times: %d Test Accuracy:%r" % (times, np.average(test_accuracy)))
        train_avg_acc.append(np.average(train_accuracy))
        test_avg_acc.append(np.average(test_accuracy))
        precision_avg.append(np.average(precision_list))
        recall_avg.append(np.average(recall_list))
        FOne_avg.append(np.average(F1_list))
        log_loss_avg.append(np.average(log_loss_list))

    print("Average Train Accuracy:%r" % (np.average(train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(test_avg_acc)))
    print("Precision Accuracy:%r" % (np.average(precision_avg)))
    print("Recall Accuracy:%r" % (np.average(recall_avg)))
    print("F1 Accuracy:%r" % (np.average(FOne_avg)))
    print("Log loss:%r" % (np.average(log_loss_avg)))
    
def tensorSVMImagesBaggingPreTrainbyGivenFeatures(images_path, timesMax, preTrainBagMax, isLG10=1, predictionType=1, vector_size=32):
    batchSz = 100
    
    # extract image features
    #featuresW0, rowsW, colsW = extractFeatures(images_path) 
         
    if isLG10 == 1:
        print('tensorSVMImagesBaggingPreTrainbyGivenFeatures on artworks which artists have more than ten painting pieces (and valid kaze features)')
    else:
        print('tensorSVMImagesBaggingPreTrainbyGivenFeatures on artworks which artists have more than five painting pieces (and valid kaze features)')
      
    # extract image features
    featuresStatistic, featuresKaze, featuresAll, predictV, rowsW, colsStatistic, colsKaze, colsAll = extractFeaturesbyGivenFile(images_path, isLG10) 
    if predictionType == 1:
        print('Feature selection is based on statistics.')
        featuresW0 = featuresStatistic
        colsW = colsStatistic
    elif predictionType == 2:
        print('Feature selection is based on kaze.')
        featuresW0 = featuresKaze
        colsW = colsKaze
    else:
        print('Feature selection is based on all.')
        featuresW0 = featuresAll
        colsW = colsAll
        
    # mimic prediction
    #y_anss = np.random.random(rowsW)
    #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
    anss = np.array(predictV)
    
    featuresW = zca_whitening_matrix(featuresW0)
    train_avg_acc = []
    test_avg_acc = []
    loss_avg_acc = []
    for times in range(timesMax):
        '''
        #Split the training data and testing data.
        train_indices = np.random.choice(len(featuresW), round(len(featuresW)*0.8), replace=False)
        test_indices = np.array(list(set(range(len(featuresW))) - set(train_indices)))
        x_vals_train = featuresW[train_indices]
        x_vals_test = featuresW[test_indices]
        
        # mimic prediction
        #y_anss = np.random.random(rowsW)
        #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
        y_vals_train = anss[train_indices]
        y_vals_test = anss[test_indices]
        '''
        x_vals_train, x_vals_test, y_vals_train, y_vals_test, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg = randomPartition(featuresW, predictV)

        #print('#1 Declare variables')
        W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW)) #A
        B = tf.Variable(tf.random.normal ([1], stddev = .1))                                       #b
        
        #print('#2 Decalre placeholder')
        img = tf.compat.v1.placeholder(tf.float32, [None, colsW]) #x_data
        ans = tf.compat.v1.placeholder(tf.float32, [None, 1]) #y_target
        
        #Declare the model output.
        model_output = tf.subtract(tf.matmul(img, W), B) #x_data, A), b)
        #Declare the necessary components for the maximum margin loss.
        l2_norm = tf.reduce_sum(tf.square(W))
        alpha = tf.constant([0.1])
        classification_term = tf.reduce_mean(tf.maximum(0., tf.subtract(1.,tf.multiply(model_output, ans))))
        loss = tf.add(classification_term, tf.multiply(alpha, l2_norm))
        
        #Declare the prediction and accuracy functions.
        prediction = tf.sign(model_output)
        accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, ans),tf.float32))
        
        ## Create the epsilon and set 0.5.
        #epsilon = tf.constant([0.5])
        #loss = tf.reduce_mean(tf.maximum(0., tf.subtract(tf.abs(tf.subtract(model_output, y_target)), epsilon)))
        ##Declare the optimizer.
        #my_opt = tf.compat.v1.train.GradientDescentOptimizer(0.075)
        #train_step = my_opt.minimize(loss)
        #init = tf.initialize_all_variables()
        #sess.run(init)
        
        #Declare the optimizer.
        my_opt = tf.compat.v1.train.GradientDescentOptimizer(0.01)
        train = my_opt.minimize(loss)
        init = tf.compat.v1.global_variables_initializer()
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())

        sumacc = 0
        loss_vec = []
        train_accuracy = []
        test_accuracy = []
        for i in range(preTrainBagMax):
            rand_index = np.random.choice(len(x_vals_train), size=batchSz)
            X = x_vals_train[rand_index]
            Y = np.transpose([y_vals_train[rand_index]])

            #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
            imgnp = X
            tanss = Y
            sess.run(train, feed_dict={img: imgnp, ans: tanss})
            #acc = sess.run(accuracy, feed_dict={img: imgnp, ans: tanss})
            temp_loss = sess.run(loss, feed_dict={img: imgnp, ans: tanss})
            loss_vec.append(temp_loss)
            train_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_train, ans: np.transpose([y_vals_train])})
            train_accuracy.append(train_acc_temp)
            test_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            test_accuracy.append(test_acc_temp)

        #print("Times: %d Train Accuracy:%r" % (times, np.average(train_accuracy)))
        #print("Times: %d Train Accuracy:%r" % (times, np.average(test_accuracy)))
        #print("Times: %d Loss :%r" % (times, np.average(loss_vec)))
        train_avg_acc.append(np.average(train_accuracy))
        test_avg_acc.append(np.average(test_accuracy))
        loss_avg_acc.append(np.average(loss_vec))
    print("Average Train Accuracy:%r" % (np.average(train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(test_avg_acc)))
    print("Average Loss:%r" % (np.average(loss_avg_acc)))
        
def tensorFFNNSample():    
    batchSz = 100
    
    print('#1')
    colsW = 784
    rowsW = 200
    # Create two variables.
    W = tf.Variable(tf.random_normal([colsW, rowsW], stddev=0.35),
                          name="weights")
    B = tf.Variable(tf.random_normal([rowsW], stddev=0.35), name="biases")

    
    print('#2')
    img = tf.placeholder(tf.float32, [batchSz, colsW])
    ans = tf.placeholder(tf.float32, [batchSz, rowsW])
    
    print('#3')
    prbs = tf.nn.softmax(tf.matmul(img, W) + B)
    xEnt = tf.reduce_mean(-tf.reduce_sum(ans * tf.log(prbs), reduction_indices =[1]))
    
    print('#4')
    train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(xEnt)
    numCorrect = tf.equal(tf.arg_max(prbs, 1), tf.arg_max(ans, 1))
    accuracy = tf.reduce_mean(tf.cast(numCorrect, tf.float32))

    print('#5')
    sess = tf.compat.v1.Session()
    sess.run(tf.compat.v1.global_variables_initializer())
    # Before starting, initialize the variables.  We will 'run' this first.
    #init = tf.initialize_all_variables()
    # Launch the graph.
    #sess = tf.compat.v1.Session()
    
    #sess.run(init)
    ignore, acc = sess.run([train, accuracy], feed_dict={img: img, ans: ans})
    print("Train Accuracy: %r" % (acc))
    #sumAcc = 0
    #sumAcc+= sess.run(accuracy, feed_dict={img: img, ans: ans})

"""
D^2 = (x-m)^T * C^-1 * (x-m)
where, 
 - D^2        is the square of the Mahalanobis distance. 
 - x          is the vector of the observation (row in a dataset), 
 - m          is the vector of mean values of independent variables (mean of each column), 
 - C^(-1)     is the inverse covariance matrix of independent variables. 
 """
def mahalanobis(x=None, data=None, cov=None):
    """Compute the Mahalanobis Distance between each row of x and the data  
    x    : vector or matrix of data with, say, p columns.
    data : ndarray of the distribution from which Mahalanobis distance of each observation of x is to be computed.
    cov  : covariance matrix (p x p) of the distribution. If None, will be computed from data.
    """
    x_minus_mu = x - np.mean(data)
    if not cov:
        cov = np.cov(np.transpose(data))
    inv_covmat = sp.linalg.inv(cov)
    left_term = np.dot(x_minus_mu, inv_covmat)
    mahal = np.dot(left_term, x_minus_mu.T)
    return mahal.diagonal()

"""
Mahalanobis distance can be used for classification problems.
Mahalanobis classifier
inputs:
    xtrain, ytrain, xtest, ytest=None
"""
class MahalanobisBinaryClassifier():
    def __init__(self, xtrain, ytrain):
        self.xtrain_pos = xtrain[ytrain == 1, :]
        self.xtrain_neg = xtrain[ytrain == 0, :]

    def predict_proba(self, xtest):
        pos_neg_dists = [(p,n) for p, n in zip(mahalanobis(xtest, self.xtrain_pos), mahalanobis(xtest, self.xtrain_neg))]
        return np.array([(1-n/(p+n), 1-p/(p+n)) for p,n in pos_neg_dists])

    def predict(self, xtest):
        return np.array([np.argmax(row) for row in self.predict_proba(xtest)])

def MahalanobisBinaryClassifierTrainingbyGivenFeatures(images_path, timesMax, isLG10=1, predictionType=1):
    batchSz = 100
    
    # extract image features
    #featuresW0, rowsW, colsW = extractFeatures(images_path) 
     
    if isLG10 == 1:
        print('MahalanobisBinaryClassifierTraining on artworks which artists have more than ten painting pieces (and valid kaze features)')
    else:
        print('MahalanobisBinaryClassifierTraining on artworks which artists have more than five painting pieces (and valid kaze features)')
      
    # extract image features
    featuresStatistic, featuresKaze, featuresAll, predictV, rowsW, colsStatistic, colsKaze, colsAll = extractFeaturesbyGivenFile(images_path, isLG10) 
    if predictionType == 1:
        print('Feature selection is based on statistics.')
        featuresW0 = featuresStatistic
        colsW = colsStatistic
    elif predictionType == 2:
        print('Feature selection is based on kaze.')
        featuresW0 = featuresKaze
        colsW = colsKaze
    else:
        print('Feature selection is based on all.')
        featuresW0 = featuresAll
        colsW = colsAll
        
    # mimic prediction
    #y_anss = np.random.random(rowsW)
    #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
    anss = np.array(predictV)  
    
    
    featuresW = zca_whitening_matrix(featuresW0)
    train_avg_acc = []
    test_avg_acc = []
    train_AUROC_avg=[]
    test_AUROC_avg=[]
    for times in range(timesMax):
        '''
        #Split the training data and testing data.
        train_indices = np.random.choice(len(featuresW), round(len(featuresW)*0.8), replace=False)
        test_indices = np.array(list(set(range(len(featuresW))) - set(train_indices)))
        xtrain = featuresW[train_indices]
        xtest = featuresW[test_indices]
        
        # mimic prediction
        #y_anss = np.random.random(rowsW)
        #anss = np.array([1 if y >0.5 else 0 for y in y_anss])
        ytrain = anss[train_indices]
        ytest = anss[test_indices]

        xtrain_pos = xtrain[ytrain == 1, :]
        xtrain_neg = xtrain[ytrain == 0, :]
        '''
        xtrain, xtest, ytrain, ytest, xtrain_pos, xtrain_neg, xtest_pos, xtest_neg, ytrain_pos, ytrain_neg, ytest_pos, ytest_neg = randomPartition(featuresW, predictV)
        
        clf = MahalanobisBinaryClassifier(xtrain, ytrain)
       
        test_pred_probs = clf.predict_proba(xtest)
        test_pred_class = clf.predict(xtest)
        
        # Pred and Truth
        test_pred_actuals = pd.DataFrame([(pred, act) for pred, act in zip(test_pred_class, ytest)], columns=['pred', 'true'])
        #print(test_pred_actuals[:5])
        
        test_truth = test_pred_actuals['true']
        test_pred = test_pred_actuals['pred']
        test_scores = np.array(test_pred_probs)[:, 1]
        #print('AUROC: ', sklearn.metrics.roc_auc_score(test_truth, test_scores))
        #print('\nConfusion Matrix: \n', sklearn.metrics.confusion_matrix(test_truth, test_pred))
        #print('\nAccuracy Score: ', sklearn.metrics.accuracy_score(test_truth, test_pred))
        #print('\nClassification Report: \n', sklearn.metrics.classification_report(test_truth, test_pred))
        test_AUROC_avg.append(roc_auc_score(test_truth, test_scores))
        test_avg_acc.append(accuracy_score(test_truth, test_pred))
        
        train_pred_probs = clf.predict_proba(xtrain)
        train_pred_class = clf.predict(xtrain)        
        
        # Pred and Truth
        train_pred_actuals = pd.DataFrame([(pred, act) for pred, act in zip(train_pred_class, ytrain)], columns=['pred', 'true'])
        #print(test_pred_actuals[:5])
        
        train_truth = train_pred_actuals['true']
        train_pred = train_pred_actuals['pred']
        train_scores = np.array(train_pred_probs)[:, 1]
        train_AUROC_avg.append(roc_auc_score(train_truth, train_scores))
        train_avg_acc.append(accuracy_score(train_truth, train_pred))
        
    print("Average Train Accuracy:%r" % (np.average(train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(test_avg_acc)))
    print("Average Train AUROC:%r" % (np.average(train_AUROC_avg)))
    print("Average Test AUROC:%r" % (np.average(test_AUROC_avg)))
    
def run():
    #print(os.path.dirname(inspect.getfile(tensorflow)))
    images_path = './images/'    
 
    featurefilename = './MoMAPaintingQArtLearnDecentArtistsMetricsVector_0705.xlsx' #statistical features from Todd + Kaze features #'./MoMAPaintingQArtLearnMetrics_Todd_0628.xlsx'
    outfile = './MoMADecentArtistsAnalysis.txt'
    imagefile = 'W1siZiIsIjE0MDQ5NyJdLFsicCIsImNvbnZlcnQiLCItcmVzaXplIDMwMHgzMDBcdTAwM2UiXV0.png'
    # Debugging...
    #W1siZiIsIjc1MTUyIl0sWyJwIiwiY29udmVydCIsIi1yZXNpemUgMzAweDMwMFx1MDAzZSJdXQ.png'
    #image = cv2.imread(str.format('./images/%s' % imagefile), 0)
    #edges = cv2.Canny(image, 100, 100)
    #print(str.format("Edge features: %r" % len(edges.flatten())))
    #tensorFFNNSample()
    
    #tensorFFNNImages(images_path) # 0.42 only training data
    isLG10V = {1, 0}
    predTypeV = {1, 2, 3}
    for isLG10 in isLG10V:
        print('isLG10 = %d' % isLG10)
        for predType in predTypeV:
            print('predType = %d' % predType)
            
            #print('tensorFFNNImagesBaggingPreTrain')
            #tensorFFNNImagesBaggingPreTrainbyGivenFeatures(featurefilename, 100, 500, isLG10, predType)
            
            #print('tensorSVMImagesBaggingPreTrain')
            #tensorSVMImagesBaggingPreTrainbyGivenFeatures(featurefilename, 100, 500, isLG10, predType)
            
            #print('MahalanobisBinaryClassifierTraining')
            #MahalanobisBinaryClassifierTrainingbyGivenFeatures(featurefilename, 100, isLG10, predType)
            
            learningbyGivenFeatures(featurefilename, 20, 500, isLG10, predType)
    
    print('Finished')
    
run()