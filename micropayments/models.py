from django.db import models
from django.utils import timezone

class Punetori(models.Model):
	pusername = models.ForeignKey('auth.User', unique=True)
	pusername.primary_key = True
	emri = models.CharField(max_length=200)
	mbiemri = models.CharField(max_length=200)
	adresa = models.CharField(max_length=200)
	telefoni = models.CharField(max_length=200)
	fid = models.ForeignKey('Filiala')

	def publish(self):
		self.save()

	def __str__(self):
		return self.emri + " " + self.mbiemri

class Klienti(models.Model):
	cid = models.AutoField(primary_key=True)
	emri = models.CharField(max_length=200)
	mbiemri = models.CharField(max_length=200)
	telefoni = models.CharField(max_length=200)

	def __str__(self):
		return str(self.cid) + " " + self.emri + " " + self.mbiemri

class Filiala(models.Model):
	fid = models.AutoField(primary_key=True)
	adresa = models.CharField(max_length=200)
	telefoni = models.CharField(max_length=200)
	shuma = models.CharField(max_length=200)
	bashkepunon = models.ManyToManyField(Klienti, blank=True)

	def __str__(self):
		return str(self.fid) + " " + self.adresa

class Derguesi(models.Model):
	did = models.OneToOneField(Klienti, primary_key=True)

	def __str__(self):
		return str(self.did)

class Marresi(models.Model):
	mid = models.OneToOneField(Klienti, primary_key=True)

	def __str__(self):
		return str(self.mid)

class Transaksioni(models.Model):
	tid = models.AutoField(primary_key=True)
	deviza = models.CharField(max_length=10)
	shuma = models.CharField(max_length=10)
	provizioni = models.CharField(max_length=10)
	data = models.DateTimeField(
			default=timezone.now)
	proceson = models.ForeignKey(Punetori)
	dergon = models.ForeignKey(Derguesi)
	merr = models.ForeignKey(Marresi)

	def __str__(self):
		return str(self.tid)
