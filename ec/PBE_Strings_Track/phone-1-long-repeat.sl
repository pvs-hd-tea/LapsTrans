(set-logic SLIA)
 
(synth-fun f ((name String)) String
    ((Start String (ntString))
     (ntString String (name " "
                       (str.++ ntString ntString)
                       (str.replace ntString ntString ntString)
                       (str.at ntString ntInt)
                       (int.to.str ntInt)
                       (str.substr ntString ntInt ntInt)))
      (ntInt Int (0 1 2 3 4 5
                  (+ ntInt ntInt)
                  (- ntInt ntInt)
                  (str.len ntString)
                  (str.to.int ntString)
                  (str.indexof ntString ntString ntInt)))
      (ntBool Bool (true false
                    (str.prefixof ntString ntString)
                    (str.suffixof ntString ntString)
                    (str.contains ntString ntString)))))


(declare-var name String)

(constraint (= (f "938-242-504") "242"))
(constraint (= (f "938-242-504") "242"))
(constraint (= (f "938-242-504") "242"))
(constraint (= (f "308-916-545") "916"))
(constraint (= (f "308-916-545") "916"))
(constraint (= (f "308-916-545") "916"))
(constraint (= (f "623-599-749") "599"))
(constraint (= (f "623-599-749") "599"))
(constraint (= (f "623-599-749") "599"))
(constraint (= (f "981-424-843") "424"))
(constraint (= (f "981-424-843") "424"))
(constraint (= (f "981-424-843") "424"))
(constraint (= (f "118-980-214") "980"))
(constraint (= (f "118-980-214") "980"))
(constraint (= (f "118-980-214") "980"))
(constraint (= (f "244-655-094") "655"))
(constraint (= (f "244-655-094") "655"))
(constraint (= (f "244-655-094") "655"))
(constraint (= (f "830-941-991") "941"))
(constraint (= (f "830-941-991") "941"))
(constraint (= (f "830-941-991") "941"))
(constraint (= (f "911-186-562") "186"))
(constraint (= (f "911-186-562") "186"))
(constraint (= (f "911-186-562") "186"))
(constraint (= (f "002-500-200") "500"))
(constraint (= (f "002-500-200") "500"))
(constraint (= (f "002-500-200") "500"))
(constraint (= (f "113-860-034") "860"))
(constraint (= (f "113-860-034") "860"))
(constraint (= (f "113-860-034") "860"))
(constraint (= (f "457-622-959") "622"))
(constraint (= (f "457-622-959") "622"))
(constraint (= (f "457-622-959") "622"))
(constraint (= (f "986-722-311") "722"))
(constraint (= (f "986-722-311") "722"))
(constraint (= (f "986-722-311") "722"))
(constraint (= (f "110-170-771") "170"))
(constraint (= (f "110-170-771") "170"))
(constraint (= (f "110-170-771") "170"))
(constraint (= (f "469-610-118") "610"))
(constraint (= (f "469-610-118") "610"))
(constraint (= (f "469-610-118") "610"))
(constraint (= (f "817-925-247") "925"))
(constraint (= (f "817-925-247") "925"))
(constraint (= (f "817-925-247") "925"))
(constraint (= (f "256-899-439") "899"))
(constraint (= (f "256-899-439") "899"))
(constraint (= (f "256-899-439") "899"))
(constraint (= (f "886-911-726") "911"))
(constraint (= (f "886-911-726") "911"))
(constraint (= (f "886-911-726") "911"))
(constraint (= (f "562-950-358") "950"))
(constraint (= (f "562-950-358") "950"))
(constraint (= (f "562-950-358") "950"))
(constraint (= (f "693-049-588") "049"))
(constraint (= (f "693-049-588") "049"))
(constraint (= (f "693-049-588") "049"))
(constraint (= (f "840-503-234") "503"))
(constraint (= (f "840-503-234") "503"))
(constraint (= (f "840-503-234") "503"))
(constraint (= (f "698-815-340") "815"))
(constraint (= (f "698-815-340") "815"))
(constraint (= (f "698-815-340") "815"))
(constraint (= (f "498-808-434") "808"))
(constraint (= (f "498-808-434") "808"))
(constraint (= (f "498-808-434") "808"))
(constraint (= (f "329-545-000") "545"))
(constraint (= (f "329-545-000") "545"))
(constraint (= (f "329-545-000") "545"))
(constraint (= (f "380-281-597") "281"))
(constraint (= (f "380-281-597") "281"))
(constraint (= (f "380-281-597") "281"))
(constraint (= (f "332-395-493") "395"))
(constraint (= (f "332-395-493") "395"))
(constraint (= (f "332-395-493") "395"))
(constraint (= (f "251-903-028") "903"))
(constraint (= (f "251-903-028") "903"))
(constraint (= (f "251-903-028") "903"))
(constraint (= (f "176-090-894") "090"))
(constraint (= (f "176-090-894") "090"))
(constraint (= (f "176-090-894") "090"))
(constraint (= (f "336-611-100") "611"))
(constraint (= (f "336-611-100") "611"))
(constraint (= (f "336-611-100") "611"))
(constraint (= (f "416-390-647") "390"))
(constraint (= (f "416-390-647") "390"))
(constraint (= (f "416-390-647") "390"))
(constraint (= (f "019-430-596") "430"))
(constraint (= (f "019-430-596") "430"))
(constraint (= (f "019-430-596") "430"))
(constraint (= (f "960-659-771") "659"))
(constraint (= (f "960-659-771") "659"))
(constraint (= (f "960-659-771") "659"))
(constraint (= (f "475-505-007") "505"))
(constraint (= (f "475-505-007") "505"))
(constraint (= (f "475-505-007") "505"))
(constraint (= (f "424-069-886") "069"))
(constraint (= (f "424-069-886") "069"))
(constraint (= (f "424-069-886") "069"))
(constraint (= (f "941-102-117") "102"))
(constraint (= (f "941-102-117") "102"))
(constraint (= (f "941-102-117") "102"))
(constraint (= (f "331-728-008") "728"))
(constraint (= (f "331-728-008") "728"))
(constraint (= (f "331-728-008") "728"))
(constraint (= (f "487-726-198") "726"))
(constraint (= (f "487-726-198") "726"))
(constraint (= (f "487-726-198") "726"))
(constraint (= (f "612-419-942") "419"))
(constraint (= (f "612-419-942") "419"))
(constraint (= (f "612-419-942") "419"))
(constraint (= (f "594-741-346") "741"))
(constraint (= (f "594-741-346") "741"))
(constraint (= (f "594-741-346") "741"))
(constraint (= (f "320-984-742") "984"))
(constraint (= (f "320-984-742") "984"))
(constraint (= (f "320-984-742") "984"))
(constraint (= (f "060-919-361") "919"))
(constraint (= (f "060-919-361") "919"))
(constraint (= (f "060-919-361") "919"))
(constraint (= (f "275-536-998") "536"))
(constraint (= (f "275-536-998") "536"))
(constraint (= (f "275-536-998") "536"))
(constraint (= (f "548-835-065") "835"))
(constraint (= (f "548-835-065") "835"))
(constraint (= (f "548-835-065") "835"))
(constraint (= (f "197-485-507") "485"))
(constraint (= (f "197-485-507") "485"))
(constraint (= (f "197-485-507") "485"))
(constraint (= (f "455-776-949") "776"))
(constraint (= (f "455-776-949") "776"))
(constraint (= (f "455-776-949") "776"))
(constraint (= (f "085-421-340") "421"))
(constraint (= (f "085-421-340") "421"))
(constraint (= (f "085-421-340") "421"))
(constraint (= (f "785-713-099") "713"))
(constraint (= (f "785-713-099") "713"))
(constraint (= (f "785-713-099") "713"))
(constraint (= (f "426-712-861") "712"))
(constraint (= (f "426-712-861") "712"))
(constraint (= (f "426-712-861") "712"))
(constraint (= (f "386-994-906") "994"))
(constraint (= (f "386-994-906") "994"))
(constraint (= (f "386-994-906") "994"))
(constraint (= (f "918-304-840") "304"))
(constraint (= (f "918-304-840") "304"))
(constraint (= (f "918-304-840") "304"))
(constraint (= (f "247-153-598") "153"))
(constraint (= (f "247-153-598") "153"))
(constraint (= (f "247-153-598") "153"))
(constraint (= (f "075-497-069") "497"))
(constraint (= (f "075-497-069") "497"))
(constraint (= (f "075-497-069") "497"))
(constraint (= (f "140-726-583") "726"))
(constraint (= (f "140-726-583") "726"))
(constraint (= (f "140-726-583") "726"))
(constraint (= (f "049-413-248") "413"))
(constraint (= (f "049-413-248") "413"))
(constraint (= (f "049-413-248") "413"))
(constraint (= (f "977-386-462") "386"))
(constraint (= (f "977-386-462") "386"))
(constraint (= (f "977-386-462") "386"))
(constraint (= (f "058-272-455") "272"))
(constraint (= (f "058-272-455") "272"))
(constraint (= (f "058-272-455") "272"))
(constraint (= (f "428-629-927") "629"))
(constraint (= (f "428-629-927") "629"))
(constraint (= (f "428-629-927") "629"))
(constraint (= (f "449-122-191") "122"))
(constraint (= (f "449-122-191") "122"))
(constraint (= (f "449-122-191") "122"))
(constraint (= (f "568-759-670") "759"))
(constraint (= (f "568-759-670") "759"))
(constraint (= (f "568-759-670") "759"))
(constraint (= (f "312-846-053") "846"))
(constraint (= (f "312-846-053") "846"))
(constraint (= (f "312-846-053") "846"))
(constraint (= (f "943-037-297") "037"))
(constraint (= (f "943-037-297") "037"))
(constraint (= (f "943-037-297") "037"))
(constraint (= (f "014-270-177") "270"))
(constraint (= (f "014-270-177") "270"))
(constraint (= (f "014-270-177") "270"))
(constraint (= (f "658-877-878") "877"))
(constraint (= (f "658-877-878") "877"))
(constraint (= (f "658-877-878") "877"))
(constraint (= (f "888-594-038") "594"))
(constraint (= (f "888-594-038") "594"))
(constraint (= (f "888-594-038") "594"))
(constraint (= (f "232-253-254") "253"))
(constraint (= (f "232-253-254") "253"))
(constraint (= (f "232-253-254") "253"))
(constraint (= (f "308-722-292") "722"))
(constraint (= (f "308-722-292") "722"))
(constraint (= (f "308-722-292") "722"))
(constraint (= (f "342-145-742") "145"))
(constraint (= (f "342-145-742") "145"))
(constraint (= (f "342-145-742") "145"))
(constraint (= (f "568-181-515") "181"))
(constraint (= (f "568-181-515") "181"))
(constraint (= (f "568-181-515") "181"))
(constraint (= (f "300-140-756") "140"))
(constraint (= (f "300-140-756") "140"))
(constraint (= (f "300-140-756") "140"))
(constraint (= (f "099-684-216") "684"))
(constraint (= (f "099-684-216") "684"))
(constraint (= (f "099-684-216") "684"))
(constraint (= (f "575-296-621") "296"))
(constraint (= (f "575-296-621") "296"))
(constraint (= (f "575-296-621") "296"))
(constraint (= (f "994-443-794") "443"))
(constraint (= (f "994-443-794") "443"))
(constraint (= (f "994-443-794") "443"))
(constraint (= (f "400-334-692") "334"))
(constraint (= (f "400-334-692") "334"))
(constraint (= (f "400-334-692") "334"))
(constraint (= (f "684-711-883") "711"))
(constraint (= (f "684-711-883") "711"))
(constraint (= (f "684-711-883") "711"))
(constraint (= (f "539-636-358") "636"))
(constraint (= (f "539-636-358") "636"))
(constraint (= (f "539-636-358") "636"))
(constraint (= (f "009-878-919") "878"))
(constraint (= (f "009-878-919") "878"))
(constraint (= (f "009-878-919") "878"))
(constraint (= (f "919-545-701") "545"))
(constraint (= (f "919-545-701") "545"))
(constraint (= (f "919-545-701") "545"))
(constraint (= (f "546-399-239") "399"))
(constraint (= (f "546-399-239") "399"))
(constraint (= (f "546-399-239") "399"))
(constraint (= (f "993-608-757") "608"))
(constraint (= (f "993-608-757") "608"))
(constraint (= (f "993-608-757") "608"))
(constraint (= (f "107-652-845") "652"))
(constraint (= (f "107-652-845") "652"))
(constraint (= (f "107-652-845") "652"))
(constraint (= (f "206-805-793") "805"))
(constraint (= (f "206-805-793") "805"))
(constraint (= (f "206-805-793") "805"))
(constraint (= (f "198-857-684") "857"))
(constraint (= (f "198-857-684") "857"))
(constraint (= (f "198-857-684") "857"))
(constraint (= (f "912-827-430") "827"))
(constraint (= (f "912-827-430") "827"))
(constraint (= (f "912-827-430") "827"))
(constraint (= (f "560-951-766") "951"))
(constraint (= (f "560-951-766") "951"))
(constraint (= (f "560-951-766") "951"))
(constraint (= (f "142-178-290") "178"))
(constraint (= (f "142-178-290") "178"))
(constraint (= (f "142-178-290") "178"))
(constraint (= (f "732-196-946") "196"))
(constraint (= (f "732-196-946") "196"))
(constraint (= (f "732-196-946") "196"))
(constraint (= (f "963-875-745") "875"))
(constraint (= (f "963-875-745") "875"))
(constraint (= (f "963-875-745") "875"))
(constraint (= (f "881-865-867") "865"))
(constraint (= (f "881-865-867") "865"))
(constraint (= (f "881-865-867") "865"))
(constraint (= (f "234-686-715") "686"))
(constraint (= (f "234-686-715") "686"))
(constraint (= (f "234-686-715") "686"))
(constraint (= (f "720-330-583") "330"))
(constraint (= (f "720-330-583") "330"))
(constraint (= (f "720-330-583") "330"))
(constraint (= (f "593-065-126") "065"))
(constraint (= (f "593-065-126") "065"))
(constraint (= (f "593-065-126") "065"))
(constraint (= (f "671-778-064") "778"))
(constraint (= (f "671-778-064") "778"))
(constraint (= (f "671-778-064") "778"))
(constraint (= (f "252-029-036") "029"))
(constraint (= (f "252-029-036") "029"))
(constraint (= (f "252-029-036") "029"))
(constraint (= (f "700-322-036") "322"))
(constraint (= (f "700-322-036") "322"))
(constraint (= (f "700-322-036") "322"))
(constraint (= (f "882-587-473") "587"))
(constraint (= (f "882-587-473") "587"))
(constraint (= (f "882-587-473") "587"))
(constraint (= (f "964-134-953") "134"))
(constraint (= (f "964-134-953") "134"))
(constraint (= (f "964-134-953") "134"))
(constraint (= (f "038-300-876") "300"))
(constraint (= (f "038-300-876") "300"))
(constraint (= (f "038-300-876") "300"))
(constraint (= (f "158-894-947") "894"))
(constraint (= (f "158-894-947") "894"))
(constraint (= (f "158-894-947") "894"))
(constraint (= (f "757-454-374") "454"))
(constraint (= (f "757-454-374") "454"))
(constraint (= (f "757-454-374") "454"))
(constraint (= (f "872-513-190") "513"))
(constraint (= (f "872-513-190") "513"))
(constraint (= (f "872-513-190") "513"))
(constraint (= (f "566-086-726") "086"))
(constraint (= (f "566-086-726") "086"))
(constraint (= (f "566-086-726") "086"))
(constraint (= (f "938-242-504") "242"))
(constraint (= (f "308-916-545") "916"))
(constraint (= (f "623-599-749") "599"))
(constraint (= (f "981-424-843") "424"))
(constraint (= (f "118-980-214") "980"))
(constraint (= (f "244-655-094") "655"))
(constraint (= (f "830-941-991") "941"))
(constraint (= (f "911-186-562") "186"))
(constraint (= (f "002-500-200") "500"))
(constraint (= (f "113-860-034") "860"))
(constraint (= (f "457-622-959") "622"))
(constraint (= (f "986-722-311") "722"))
(constraint (= (f "110-170-771") "170"))
(constraint (= (f "469-610-118") "610"))
(constraint (= (f "817-925-247") "925"))
(constraint (= (f "256-899-439") "899"))
(constraint (= (f "886-911-726") "911"))
(constraint (= (f "562-950-358") "950"))
(constraint (= (f "693-049-588") "049"))
(constraint (= (f "840-503-234") "503"))
(constraint (= (f "698-815-340") "815"))
(constraint (= (f "498-808-434") "808"))
(constraint (= (f "329-545-000") "545"))
(constraint (= (f "380-281-597") "281"))
(constraint (= (f "332-395-493") "395"))
(constraint (= (f "251-903-028") "903"))
(constraint (= (f "176-090-894") "090"))
(constraint (= (f "336-611-100") "611"))
(constraint (= (f "416-390-647") "390"))
(constraint (= (f "019-430-596") "430"))
(constraint (= (f "960-659-771") "659"))
(constraint (= (f "475-505-007") "505"))
(constraint (= (f "424-069-886") "069"))
(constraint (= (f "941-102-117") "102"))
(constraint (= (f "331-728-008") "728"))
(constraint (= (f "487-726-198") "726"))
(constraint (= (f "612-419-942") "419"))
(constraint (= (f "594-741-346") "741"))
(constraint (= (f "320-984-742") "984"))
(constraint (= (f "060-919-361") "919"))
(constraint (= (f "275-536-998") "536"))
(constraint (= (f "548-835-065") "835"))
(constraint (= (f "197-485-507") "485"))
(constraint (= (f "455-776-949") "776"))
(constraint (= (f "085-421-340") "421"))
(constraint (= (f "785-713-099") "713"))
(constraint (= (f "426-712-861") "712"))
(constraint (= (f "386-994-906") "994"))
(constraint (= (f "918-304-840") "304"))
(constraint (= (f "247-153-598") "153"))
(constraint (= (f "075-497-069") "497"))
(constraint (= (f "140-726-583") "726"))
(constraint (= (f "049-413-248") "413"))
(constraint (= (f "977-386-462") "386"))
(constraint (= (f "058-272-455") "272"))
(constraint (= (f "428-629-927") "629"))
(constraint (= (f "449-122-191") "122"))
(constraint (= (f "568-759-670") "759"))
(constraint (= (f "312-846-053") "846"))
(constraint (= (f "943-037-297") "037"))
(constraint (= (f "014-270-177") "270"))
(constraint (= (f "658-877-878") "877"))
(constraint (= (f "888-594-038") "594"))
(constraint (= (f "232-253-254") "253"))
(constraint (= (f "308-722-292") "722"))
(constraint (= (f "342-145-742") "145"))
(constraint (= (f "568-181-515") "181"))
(constraint (= (f "300-140-756") "140"))
(constraint (= (f "099-684-216") "684"))
(constraint (= (f "575-296-621") "296"))
(constraint (= (f "994-443-794") "443"))
(constraint (= (f "400-334-692") "334"))
(constraint (= (f "684-711-883") "711"))
(constraint (= (f "539-636-358") "636"))
(constraint (= (f "009-878-919") "878"))
(constraint (= (f "919-545-701") "545"))
(constraint (= (f "546-399-239") "399"))
(constraint (= (f "993-608-757") "608"))
(constraint (= (f "107-652-845") "652"))
(constraint (= (f "206-805-793") "805"))
(constraint (= (f "198-857-684") "857"))
(constraint (= (f "912-827-430") "827"))
(constraint (= (f "560-951-766") "951"))
(constraint (= (f "142-178-290") "178"))
(constraint (= (f "732-196-946") "196"))
(constraint (= (f "963-875-745") "875"))
(constraint (= (f "881-865-867") "865"))
(constraint (= (f "234-686-715") "686"))
(constraint (= (f "720-330-583") "330"))
(constraint (= (f "593-065-126") "065"))
(constraint (= (f "671-778-064") "778"))
(constraint (= (f "252-029-036") "029"))
(constraint (= (f "700-322-036") "322"))
(constraint (= (f "882-587-473") "587"))
(constraint (= (f "964-134-953") "134"))
(constraint (= (f "038-300-876") "300"))
(constraint (= (f "158-894-947") "894"))
(constraint (= (f "757-454-374") "454"))
(constraint (= (f "872-513-190") "513"))
(constraint (= (f "566-086-726") "086"))

(check-synth)
