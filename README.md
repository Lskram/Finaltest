# 🪴🌻🏵️ FINAL PROJECT 🏵️🌻🪴 ˊˎ -
## 👨‍💼🏭 &larr; โปรเจคพนักงานบริษัทและแผนก
## ⚙️ ``` Coding Project  ``` 🔧
###### 🖥 ADMIN USERNAME 🖥
```shell
admin12
```
###### 🔐 ADMIN PASSWORD 🔐
```shell
1212
```

## 🪴🌻 1. การสร้างคลาสแผนกขึ้นมาเปรียบเป็น Category ที่คอยจัดหมวดหมู่สิ่งนั้นให้อยู่ในพื้นที่ที่เราต้องการให้แสดง
```shell
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
```


## 🪴🌻  2. ความสัมพันธ์แบบ one-to-many
```shell
  class Classes(models.Model):
    name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    age = models.IntegerField()
    Educationlevel = models.CharField(max_length=256)
    department = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```


### 🖼💾 รูปความสัมพันธ์แบบ one-to-many
#### ⚠ ความสัมพันธ์แบบ one-to-many นั้นเป็นความสัมพันธ์ระหว่าง models เช่น พนักงาน 1 คน สามารถมีแผนกได้เพียงแผนกเดียวเท่านั้น แต่ว่าแผนก 1 แผนก สามารถมีพนักงานได้หลายคน
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B8%A3%E0%B8%B9%E0%B8%9B%20One%20to%20many.png)


# 🌻🌗🌘````````` 3.รูปภาพประกอบ ````````` 🌒🌓🌞

### 🌳🌻 3.1 รูปเกี่ยวกับบริษัทและรายชื่อพนักงานบริษัททั้งหมด 🌻🌳
#### 🌴การแสดงผลรายชื่อพนักงานในบริษัททั้งหมดภายใต้การทำงานของ Django 🦎 ร่วมกับ Vscode และ Python🐍
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%9E%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B8%AB%E0%B8%A1%E0%B8%94.png)


### 🌳🌻 3.2 รูปเกี่ยวกับผู้ดูแลแอดมินพนักงานบริษัททั้งหมด 🌻🌳
#### 🌴ในการทำงานส่วนนี้สามารถเพิ่ม แผนก,ข้อมูลของพนักงานเพิ่มเข้ามาได้อย่างไม่จำกัด และแสดงข้อมูลพนักงานทั้งหมดสามาถลบและแก้ไขได้ตลอดเวลา!
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%94%E0%B8%B9%E0%B9%81%E0%B8%A5%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A.png)


### 🌳🌻 3.3 รูปภาพเกี่ยวกับแผนกในบริษัททั้งหมด 🌻🌳
#### 🦋 มีทั้งหมด 3 แผนกดดังต่อไปนี้ 🦋
- [x] แผนกจัดซื้อ 💰
- [x] แผนกจัดหาลูกค้า 🎓
- [x] บริการหลังขาย 🖥
##### 🦋🌳3.3.1 รูปภาพเกี่ยวกับแผนกจัดซื้อในบริษัททั้งหมด 🌳🦋
###### 🌴ในการทำงานส่วนนี้สามารถเเสดง แผนกจัดซื้อ,ข้อมูลของพนักงาน ทั้งหมดได้ในส่วนนี้
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B9%81%E0%B8%9C%E0%B8%99%E0%B8%81%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD.png)


##### 🦋🌳3.3.2 รูปภาพเกี่ยวกับแผนกจัดหาลูกค้าในบริษัททั้งหมด 🌳🦋
###### 🌴ในการทำงานส่วนนี้สามารถเเสดง แผนกจัดหาลูกค้า,ข้อมูลของพนักงาน ทั้งหมดได้ในส่วนนี้
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B9%81%E0%B8%9C%E0%B8%99%E0%B8%81%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%AB%E0%B8%B2%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%84%E0%B9%89%E0%B8%B2.png)


##### 🦋🌳3.3.3 รูปภาพเกี่ยวกับแผนกบริการหลังการขายในบริษัททั้งหมด 🌳🦋
###### 🌴ในการทำงานส่วนนี้สามารถเเสดง แผนกบริการหลังการขาย,ข้อมูลของพนักงาน ทั้งหมดได้ในส่วนนี้
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B9%81%E0%B8%9C%E0%B8%99%E0%B8%81%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B8%B2%E0%B8%A2.png)


### 🌳🌻 4 รูปเกี่ยวกับบริษัท 🌻🌳
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%A9%E0%B8%B1%E0%B8%97.png)



### 🌳🌻 5. GitHub ร่วมกับ Supabase,Versel 🌻🌳
#### 🌴เรียกได้ว่า Github เป็นพระเอกที่สำคัญในการเข้าไปใช้งาน Supabase,Versel ต่างให้บริการกันทำให้ง่ายต่อนักเขียนโปรแกรมในการพัฒนาเว็บไซต์เป็นอย่างมาก ไม่ว่าจะเป็นการสร้างตารางและสามารถบันทึกและจัดเก็บข้อมูลไว้ใน Supabase หรือการอัพ Deploy เว็บของเราขึ้นผ่าน Vercel ทำให้คนอื่นๆสามารถเห็นเว็บไซต์ที่เราเขียนขึ้นมาได้ใช้งานกันอย่างฟรีๆ นั่นเอง
### 🔎⚙ 5.1 รูปเกี่ยวกับการจัดการตารางใน Supabase 🔎⚙
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%88%E0%B8%B2%E0%B8%81%20supabase.png)
### 🔎⚙ 5.2 รูปเกี่ยวกับการจัดการDeployใน Vercel 🔎⚙
📌 ![image](https://github.com/Lskram/Finaltest/blob/main/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%A0%E0%B8%B2%E0%B8%9E/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%88%E0%B8%B2%E0%B8%81%20vercel.png)
#  🌼🌷💐🌻 ขอบคุณครับ 🌻💐🌷🌼


## 💾 CREDIT
**[💻 YOUTUBE :   Phisan Sookkhee](https://www.youtube.com/watch?v=EC6k9KduQYU&list=PLUD6z42fSjQq785dtC6bl9BTSlO-_EjY9) ❗️**
