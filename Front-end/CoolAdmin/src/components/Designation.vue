<script setup xmlns="http://www.w3.org/1999/html">


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <div class="row form-group" style="color: #6f42c1; font-size: 1.8em">
          <div class="col col-md-9">
            <div class="form-check-inline form-check" v-for="atelier in ateliers" :key="atelier.id">
                <input type="radio"  :value="atelier" id="inline-radio1" style="width: 30px" name="inline-radios"  v-model="currentAtelier" @change="selectAtelier(atelier)">{{atelier.nom}}
            </div>
          </div>
        </div>
        <div class="form-group">
          <label for="cc-number" class="control-label mb-1">Mois</label>
          <input  type="month" style="height: 50px; width: 300px" class="form-control" aria-required="true" aria-invalid="false" v-model="currentMois" @change="selectMois(currentMois)">


        </div>
        <button type="button" class="btn btn-outline-success btn-lg" style="margin-bottom:70px; font-size: 1.8em" @click="this.designation.atelier_id=this.currentAtelier.id ; this.designation.mois=this.currentMois" data-toggle="modal" data-target="#Add"><i class="fa fa-plus-square"></i> Ajouter</button>
        <div class="row">

          <div class="table-responsive table--no-card m-b-30">
            <table class="table table-borderless table-striped table-earning">
              <thead >
              <tr>
                <th>Date</th>
                <th>Travail</th>
                <th>Action</th>
              </tr>
              </thead>
              <tbody>

                <!-- Designations de la catégorie -->
                <template v-for="item in designations" >
                  <tr style="font-size: 1.5em" v-if=" item.atelier === currentAtelier.nom &&  item.mois === currentMois">
                    <td>{{ item.date }}</td>
                    <td>{{ item.travail }}</td>
                    <td>
                      <i class="fa fa-pencil-alt" style="font-size: 1.1em; color: #c69500; margin-right: 20px" @click="showEditModal(item); this.currentDesignation.atelier_id=this.currentAtelier.id" data-toggle="modal" data-target="#Edit"></i>
                      <i class="fa fa-trash-alt" style="font-size: 1.1em; color: #bd2130" @click="deleteDesignation(item.id)"></i>
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
          <h5 class="modal-title" id="mediumModalLabel">Designation</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Nouvelle Designation</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="addDesignation">
                  <div class="form-group">
                    <label  class="control-label mb-1">Date</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="designation.date">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Travail</label>
                    <input  type="number" class="form-control cc-name valid" v-model="designation.travail">
                  </div>
                  <div v-if="Message" class="alert alert-success">
                    {{ Message }}
                  </div>
                  <div v-if="errorMessage" class="alert alert-danger">
                    {{ errorMessage }}
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
          <h5 class="modal-title" id="mediumModalLabel">Designation</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Modification Designation</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="editDesignation(currentDesignation.id)">
                  <div class="form-group">
                    <label  class="control-label mb-1">Date</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="currentDesignation.date">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Mois</label>
                    <input  type="month" class="form-control" aria-required="true" aria-invalid="false" v-model="currentDesignation.mois">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Travail</label>
                    <input  type="number" class="form-control cc-name valid" v-model="currentDesignation.travail">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Atelier</label>
                    <select class="form-control" v-model="currentDesignation.atelier_id">
                      <option v-for="atelier in ateliers" :key="atelier.id" :value="atelier.id">
                        {{ atelier.nom }}
                      </option>
                    </select>
                  </div>
                  <div v-if="ModiferrorMessage" class="alert alert-danger">
                    {{ ModiferrorMessage }}
                  </div>
                  <div v-if="ModifMessage" class="alert alert-success">
                    {{ ModifMessage }}
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
      designation:{
        date:'',
        travail:'',
        atelier_id:'',
        mois:'',
      },
      currentDesignation: {},
      currentAtelier: JSON.parse(localStorage.getItem('atelier')),
      currentMois: localStorage.getItem('mois'),
      RecDesignation: {},
      ateliers:[],
      designations:[],
      Message: null,
      errorMessage: null,
      ModifMessage: null,
      ModiferrorMessage: null,
    };
  },
  mounted() {
    this.listDesignation();
    this.listAtelier();
  },
  methods: {
    async listDesignation(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/designations')
        this.designations=response.data
        if (this.designations.length > 0) {
          this.RecDesignation = this.designations[this.designations.length - 1];
        } else {
          this.RecDesignation = {};
        }
      }catch (error){
        console.error(error)
      }
    },

    async listAtelier() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ateliers');
        this.ateliers = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addDesignation() {
      this.designation.atelier_id=this.currentAtelier.id
      this.designation.mois=this.currentMois
      if(0<this.designation.date && this.designation.date<=31 && this.designation.travail>0){
        const formData = new FormData();
        formData.append('date', this.designation.date);
        formData.append('travail', this.designation.travail);
        formData.append('atelier_id', this.designation.atelier_id);
        formData.append('mois', this.designation.mois);

        try {
          await axios.post('http://127.0.0.1:5000/api/michelin/designations', formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.Message="Enregistrement reussi"
          this.errorMessage=null
          this.designation = {};
          await this.listDesignation();
        } catch (error) {
          console.error('Error:', error);
        }
      }else{
        this.Message=null
        this.errorMessage="Date ou Travail incorrect"
      }

    },
    async editDesignation(id) {
      if(0<this.currentDesignation.date && this.currentDesignation.date<=31 && this.currentDesignation.travail>0){
        const formData = new FormData();
        formData.append('date', this.currentDesignation.date);
        formData.append('travail', this.currentDesignation.travail);
        formData.append('atelier_id', this.currentDesignation.atelier_id)
        formData.append('mois', this.currentDesignation.mois)

        try {
          await axios.put(`http://127.0.0.1:5000/api/michelin/updateDesignation/${id}`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.ModiferrorMessage=null
          this.ModifMessage="Modification reussi"
          this.currentDesignation = {};
          await this.listDesignation();
          localStorage.setItem('mois', this.currentMois )
        } catch (error) {
          console.error('Error:', error);
        }
      }
        else{
        this.ModifMessage=null
        this.ModiferrorMessage = 'Date ou travail Incorrect';

      }
    },
    async deleteDesignation(id) {
      try {
        await axios.delete(`http://127.0.0.1:5000/api/michelin/deleteDesignation/${id}`);
        await this.listDesignation();
      } catch (error) {
        console.error(error);
      }
    },
    showEditModal(designation) {
      this.currentDesignation = { ...designation };
    },

    selectAtelier(newAtelier) {
      this.currentAtelier = newAtelier;

      // Mettre à jour dans localStorage
      localStorage.setItem('atelier', JSON.stringify(this.currentAtelier));

    },

    selectMois(newMois) {
      this.currentMois = newMois;

      // Mettre à jour dans localStorage
      localStorage.setItem('mois',this.currentMois);

    },
  },


  props:{}
};
</script>

<style scoped>

</style>