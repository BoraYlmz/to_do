# To-Do Uygulama Projesi / To-Do Application Project

### [Türkçe](#turkce)
### [English](#english)

---

## Türkçe / Turkish <a name="turkce"></a>

Bu proje, günlük iş akışlarındaki kısa süreli (yaklaşık 15-30 dakika) boş zamanlarda geliştirdiğim ilk Tkinter tabanlı arayüz projesidir. Projenin başlangıç fikri, mevcut çalışma ortamımızda kullandığımız farklı uygulamaları tek bir platformda birleştirmenin nasıl bir deneyim yaratabileceği ve bu sürecin neler gerektireceği üzerine şekillenmiştir. Bu proje, söz konusu fikrin ilk modülünü oluşturmaktadır.

Bu modül, kullanıcıların görevlerini **"Başlamamış"**, **"İşlemde"** ve **"Bitti"** olmak üzere üç farklı sütunda listeleyebilmelerini sağlar. Her bir görev, detaylı açıklamalar ve eklenebilir yorumlar içermektedir. Modül, mevcut görevlerin durumunu takip etmeyi amaçlayan bir görev atama aracıdır.

## Proje Ekran Görüntüleri:
<div style="display: flex; justify-content: space-between; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/51352d6d-e1ec-48df-9dde-5aea06eccf5e" alt="login_panel" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/a558194a-4931-472c-91a1-8cd298c5183b" alt="mail_panel" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/4921feb9-64f2-4f2b-b5ee-c813171d61cd" alt="mail_detail" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/9097d0be-d0f6-4ae1-83de-daeab6089865" alt="new_mail" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/bcf42d10-a19d-43f2-9827-3f3dd9027edb" alt="message_box_example" style="width: 300px;" />
</div>

## Eksik Yönler ve Gelecek Geliştirme Fikirleri:

### **Proje Durumu:**
Bu proje, planlanan işlevlerin bazıları tamamlanmamış ve yarım kalmış bir projedir. Ancak, mevcut haliyle kullanım için uygundur. Geliştirilecek bazı özellikler aşağıda belirtilmiştir.

### **Eksiklikler ve Geliştirme Alanları:**
1. **Kullanıcı Kayıt Modülü Eksikliği / Missing User Registration Module:**
   Proje, kullanıcı kaydı modülüne sahip değildir. İki farklı fikir arasında kalınmış ve her iki seçenek de henüz uygulanmamıştır:
   - Manuel kullanıcı girişi ile tanımlama (yetki verilmemişlerin sisteme girişi engelleme).
   - Lokal ağda bulunan kullanıcı adı ile otomatik giriş yapma ve loglama işlemi.

2. **Veritabanı Sorunu:**
   Proje geliştirilirken, TinyDB kullanılarak lokal bir veritabanı yapılandırılmıştır. Başlangıçta, görev yorumlarının veritabanını gereksiz yere büyütebileceği ve ilerleyen süreçte sorgulama işlemlerini zorlaştırabileceği düşüncesiyle, her görev için ayrı bir JSON dosyasında yorumlar tutulmaya karar verilmiştir. Ancak proje ilerledikçe, bu yaklaşımın gereksiz olduğu anlaşılmıştır. Veritabanı yapısında yapılacak değişiklikle birlikte, bu veri için yeni bir tablo oluşturulmalı ve ilgili kod güncellenmelidir.

3. **Canlı (Live) Mail Güncellemeleri:**
   Yeni gönderilen veya güncellenen görevler için **canlı güncelleme** özelliği eksiktir. Bunun için yeni bir thread açılacak ve kullanıcıyı ilgilendiren görevler taranarak ekranın otomatik olarak güncellenmesi sağlanacaktır. Bu özellik, kullanıcı bazlı görev güncellemeleri ve yorumların takip edilmesi için önemli olacaktır.

4. **Kullanıcı Ayarları ve Geçiş Modülü:**
   `usersetting.cfg` dosyası, kullanıcılar arasında geçiş yapmak amacıyla basitçe bırakılmıştır. Gelecekte, kullanıcı bilgilerini baz alarak bir giriş anahtarı üretme işlemi ve şifreli giriş mekanizması eklenmesi planlanmıştır.

5. **Görev Atama Modülü:**
   Şu anda görevler yalnızca bireysel olarak atanmaktadır. **Çoklu görev atama** özelliği eklenerek birden fazla kişi aynı ve ortak görev ataması yapılabilir.

### **Proje Güncelleme Durumu:**
Güncellemeler, çeşitli sebeplerden ötürü durdurulmuş olup, modül henüz merkezi bir hub uygulamasına dönüştürülmemiştir. Ancak mevcut haliyle modül işlevsel olup kullanılabilir durumdadır. Bununla birlikte, proje üzerinde gerçekleştirilebilecek geliştirmeler ve giderilmesi gereken eksiklikler yukarıda detaylı bir şekilde sıralanmıştır.

---

## English / İngilizce <a name="english"></a>

This project is my first Tkinter-based GUI application developed during short free periods (approximately 15-30 minutes) in my daily workflow. The initial idea behind the project was to combine the various applications used in our work environment into a single platform and explore what this experience would be like, as well as what it would require. This project represents the first module of that idea.

This module allows users to list their tasks in three different columns: **"Not Started"**, **"In Progress"**, and **"Completed"**. Each task includes detailed descriptions and the ability to add comments. The module is a task assignment tool designed to track the current status of tasks.

## Project Screenshots:
<div style="display: flex; justify-content: space-between; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/51352d6d-e1ec-48df-9dde-5aea06eccf5e" alt="login_panel" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/a558194a-4931-472c-91a1-8cd298c5183b" alt="mail_panel" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/4921feb9-64f2-4f2b-b5ee-c813171d61cd" alt="mail_detail" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/9097d0be-d0f6-4ae1-83de-daeab6089865" alt="new_mail" style="width: 300px;" />
  <img src="https://github.com/user-attachments/assets/bcf42d10-a19d-43f2-9827-3f3dd9027edb" alt="message_box_example" style="width: 300px;" />
</div>

## Missing Features and Future Development Ideas:

### **Project Status:**
This project is incomplete, and some planned features are not yet implemented. However, it is functional and ready for use. The following features are still in development.

### **Missing Features and Areas for Development:**
1. **Missing User Registration Module:**
   The project lacks a user registration module. Two options have been considered but not yet implemented:
   - Manual user login and assignment (restrict access for unauthorized users).
   - Automatic login and logging via the local network username.

2. **Database Issue:**
   During development, **TinyDB** was used for the local database. Initially, it was decided to store comments for each task in separate JSON files to avoid bloating the database and complicating queries later. However, as the project progressed, it became clear that this approach was unnecessary. A new table should be created in the database, and the code should be updated accordingly.

3. **Live Mail Updates:**
   The project currently lacks live updates for newly sent or updated tasks. A new thread will be created to scan tasks related to the user, and the interface will be updated automatically. This feature is essential for task-based updates and comment tracking.

4. **User Settings and Transition Module:**
   The `usersetting.cfg` file is a simple solution for switching between users. Future updates will include a mechanism for generating a login key based on user information and implementing encrypted login.

5. **Task Assignment Module:**
   Currently, tasks are assigned individually. A **bulk task assignment** feature will be added to allow multiple users to be assigned the same task.

### **Project Update Status:**
Updates have been paused for various reasons, and the module has not yet been transformed into a centralized hub application. However, the module is functional and usable in its current form. The project’s development and areas for improvement are outlined above.

---

