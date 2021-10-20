from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    # patients = models.ManyToManyField(Patient)    -> 이렇게도 가능. 참조 관계가 바뀌는 것일 뿐  
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    # ManyToManyField 작성  -> 중개모델 직접 작성하지 않아도 해당하는 중개 필드 자동으로작성된다. 
    # doctors = models.ManyToManyField(Doctor) # , through='Reservation'

    # related_name변경 
    doctors = models.ManyToManyField(Doctor, related_name='patient')    

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'


patient1 = Patient.objects.get(pk=1)

patient1.reservation_set.all()
# <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

patient1.doctors.all()
# <QuerySet [<Doctor: 1번 의사 justin>]>



# 실제는 여기서 부터 작성 + 앞에 patient랑 doctor는 정의해줘야함 
# 예약생성 - 참조 (patient1이 doctor1에게 예약)
patient1.doctors.add(doctor1)
patient1.doctors.all()
doctor1.patient_set.all() 

# 예약삭제 (참조)
patient2.doctors.remove(doctor1)
patient2.doctors.all()
doctor1.patinet_set.all()


# 예약생성 - 역참조

# 예약삭제 - 역참조 



# related_name 설정 이후 :
# doctor1.patient_set.all() 이 아니라 
doctor1.patient.all()