member1 = {"id":10,
            "nama":"Reno",
            "pekerjaan":"mahasiswa",
            "status":"hired"
            }
member2 = {"id":20,
            "nama":"Beni",
            "pekerjaan":"nganggur",
            "status":"fired"
            }

memberlist = {101:member1,102:member2}
print(memberlist)
print(memberlist[102]["nama"])

print(member1["id"],". Nama:",member1["nama"])
print(member1.keys())
print(member1.values())
print(member1.items())
