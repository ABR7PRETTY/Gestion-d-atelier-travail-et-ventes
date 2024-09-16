<script setup xmlns="http://www.w3.org/1999/html">


import Atelier from "@/components/Atelier.vue";
</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <div class="row form-group" style="color: #6f42c1; font-size: 1.8em">
          <div class="col col-md-9">
            <div class="form-check-inline form-check" v-for="atelier in ateliers" :key="atelier.id">
              <input type="radio"  :value="atelier" id="inline-radio1" style="width: 30px" name="inline-radios" @change="selectAtelier(atelier)" v-model="currentAtelier" >{{atelier.nom}}
            </div>
          </div>
        </div>
        <button type="button" class="btn btn-outline-success btn-lg" style="margin-bottom:70px; font-size: 1.8em" @click="this.apprenti.atelier_id=this.currentAtelier.id" data-toggle="modal" data-target="#Add"><i class="fa fa-plus-square"></i> Ajouter</button>
        <div class="row">

          <div class="table-responsive table--no-card m-b-30">
            <table class="table table-borderless table-striped table-earning">
              <thead >
              <tr>
                <th>Image</th>
                <th>Nom</th>
                <th>Prenom</th>
                <th>Age</th>
                <th>Grade</th>
                <th>Tuteur</th>
                <th>Action</th>
              </tr>
              </thead>
              <tbody>

              <!-- Apprentis de la catégorie -->
              <template v-for="item in apprentis" >
                <tr style="font-size: 1.5em" v-if="item.atelier === currentAtelier.nom">
                  <td><img class="card-img-top" :src="getUrlImage(item.image)" :alt="item.nom"></td>
                  <td>{{ item.nom }}</td>
                  <td>{{ item.prenom }}</td>
                  <td>{{ item.age }}</td>
                  <td>{{ item.grade }}</td>
                  <td>{{ item.tuteur }}</td>
                  <td>
                    <i class="fa fa-pencil-alt" style="font-size: 1.1em; color: #c69500; margin-right: 20px" @click="showEditModal(item)" data-toggle="modal" data-target="#Edit"></i>
                    <i class="fa fa-trash-alt" style="font-size: 1.1em; color: #bd2130" @click="deleteApprenti(item.id)"></i>
                  </td>
                </tr>
              </template>
              </tbody>

            </table>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="copyright">
              <marquee style=" margin-top: 2px">
                <p style="color: rgba(102,102,102,0.89)"> @ABR7  &emsp; 00228 93 38 25 76</p>
              </marquee>
              <p>Copyright © 2018 Colorlib. All rights reserved. Template by <a href="https://colorlib.com">Colorlib</a>.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


  <div class="modal fade" id="Add" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Apprenti</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Nouvel Apprenti</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="addApprenti">
                  <div class="form-group">
                    <label  class="control-label mb-1">Nom</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="apprenti.nom">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Prenom</label>
                    <input  type="text" class="form-control cc-name valid" v-model="apprenti.prenom">
                  </div>
                  <div class="form-group">
                    <label  class="control-label mb-1">Age</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="apprenti.age">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Grade</label>
                    <select class="form-control" v-model="apprenti.grade">
                      <option value="Debutant">
                        Débutant
                      </option>
                      <option value="Senior">
                        Senior
                      </option>
                      <option value="Responsable">
                        Responsable
                      </option>
                    </select>
                    <div class="form-group">
                      <label  class="control-label mb-1">Tuteur</label>
                      <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="apprenti.tuteur">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Atelier</label>
                    <select class="form-control" v-model="apprenti.atelier_id">
                      <option v-for="atelier in ateliers" :key="atelier.id" :value="atelier.id">
                        {{ atelier.nom }}
                      </option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Image</label>
                    <input  type="file" class="form-control cc-number identified visa" @change="onImageChange">
                  </div>
                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-reply"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Retour </h4></i>
                    <button type="submit" > <i class="fa fa-check"  style="font-size: 3em; color: #00b26f" ><h4>Save </h4> </i> </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="modal fade" id="Edit" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Apprenti</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Modification Apprenti</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="editApprenti(currentApprenti.id)">
                  <div class="form-group">
                    <label  class="control-label mb-1">Nom</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="currentApprenti.nom">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Prenom</label>
                    <input  type="text" class="form-control cc-name valid" v-model="currentApprenti.prenom">
                  </div>
                  <div class="form-group">
                    <label  class="control-label mb-1">Age</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="currentApprenti.age">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Grade</label>
                    <select class="form-control" v-model="currentApprenti.grade">
                      <option value="Debutant">
                        Débutant
                      </option>
                      <option value="Senior">
                        Senior
                      </option>
                      <option value="Responsable">
                        Responsable
                      </option>
                    </select>
                    <div class="form-group">
                      <label  class="control-label mb-1">Tuteur</label>
                      <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="currentApprenti.tuteur">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Atelier</label>
                    <select class="form-control" v-model="currentApprenti.atelier_id">
                      <option v-for="atelier in ateliers" :key="atelier.id" :value="atelier.id">
                        {{ atelier.nom }}
                      </option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Image</label>
                    <input  type="file" class="form-control cc-number identified visa" @change="OnImageChangeEdit">
                  </div>

                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-reply"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Cancel </h4></i>
                    <button type="submit"> <i class="fa fa-check"  style="font-size: 3em; color: #00b26f" ><h4>Save </h4> </i> </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data(){
    return{
      apprenti:{
        nom:'',
        prenom:'',
        age:'',
        grade:'',
        tuteur:'',
        image:null,
        atelier_id:'',
      },
      currentApprenti: {},
      currentAtelier: JSON.parse(localStorage.getItem('atelier')),
      ateliers:[],
      apprentis:[],
    };
  },
  mounted() {
    this.listApprenti();
    this.listAtelier()
  },
  methods: {
    onImageChange(event){
      this.apprenti.image=event.target.files[0];
    },
    OnImageChangeEdit(event){
      this.currentApprenti.image=event.target.files[0];
    },
    async listApprenti(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/apprentis')
        this.apprentis=response.data
      }catch (error){
        console.error(error)
      }
    },
    async listAtelier() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ateliers');
        this.ateliers = response.data;
        console.log(this.currentAtelier)
      } catch (error) {
        console.error(error);
      }
    },
    getUrlImage(monImage) {
      return 'http://127.0.0.1:5000/static/' + monImage;
    },
    async addApprenti() {
      const formData = new FormData();
      formData.append('nom', this.apprenti.nom);
      formData.append('prenom', this.apprenti.prenom);
      formData.append('age', this.apprenti.age);
      formData.append('grade', this.apprenti.grade);
      formData.append('tuteur', this.apprenti.tuteur);
      formData.append('image', this.apprenti.image);
      formData.append('atelier_id', this.apprenti.atelier_id);

      try {
        await axios.post('http://127.0.0.1:5000/api/michelin/apprentis', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        this.apprenti = {};
        await this.listApprenti();
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async editApprenti(id) {
      const formData = new FormData();
      formData.append('nom', this.currentApprenti.nom);
      formData.append('prenom', this.currentApprenti.prenom);
      formData.append('age', this.currentApprenti.age);
      formData.append('grade', this.currentApprenti.grade);
      formData.append('tuteur', this.currentApprenti.tuteur);
      formData.append('atelier_id', this.currentApprenti.atelier_id);
      if (this.currentApprenti.image) {
        formData.append('image', this.currentApprenti.image);
      }

      try {
        await axios.put(`http://127.0.0.1:5000/api/michelin/updateApprenti/${id}`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        this.currentApprenti = {};
        await this.listApprenti();
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async deleteApprenti(id) {
      try {
        await axios.delete(`http://127.0.0.1:5000/api/michelin/deleteApprenti/${id}`);
        await this.listApprenti();
      } catch (error) {
        console.error(error);
      }
    },
    showEditModal(apprenti) {
      this.currentApprenti = { ...apprenti };
    },

    selectAtelier(newAtelier) {
      this.currentAtelier = newAtelier;

      // Mettre à jour dans localStorage
      localStorage.setItem('atelier', JSON.stringify(this.currentAtelier));

    },

  },


  props:{}
};
</script>

<style scoped>

</style>