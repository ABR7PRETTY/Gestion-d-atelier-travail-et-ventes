<script setup>


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <button type="button" class="btn btn-outline-success btn-lg" style="margin-bottom:70px; font-size: 1.8em" data-toggle="modal" data-target="#Add"><i class="fa fa-plus-square"></i> Ajouter</button>
        <div class="row">

          <div class="col-md-4" v-for="(item, index) in categories" :key="index">
            <div class="card" >
              <img class="card-img-top" style="height: 350px" :src="getUrlImage(item.image)" :alt="item.libelle">
              <div class="card-body">
                <h3>{{item.libelle}}</h3>
                <p>{{item.description}}</p>
                <div class="row" style="float: right ; margin-right: 20px">
                  <i class="fa fa-pencil-alt"  style="font-size: 1.8em; color: #c69500; margin-right: 20px" @click="showEditModal(item)" data-toggle="modal" data-target="#Edit"></i>
                  <i class="fa fa-trash-alt"  style="font-size: 1.8em; color: #bd2130" @click="deleteCategorie(item.id)"></i>
                </div>
              </div>
            </div>
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
          <h5 class="modal-title" id="mediumModalLabel">Categorie</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Nouvelle Categorie</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="addCategorie">
                  <div class="form-group">
                    <label  class="control-label mb-1">Libelle</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="categorie.libelle">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Description</label>
                    <input  type="text" class="form-control cc-name valid" v-model="categorie.description">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Image</label>
                    <input  type="file" class="form-control cc-number identified visa" @change="onImageChange">
                  </div>
                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-times"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Cancel </h4></i>
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

  <div class="modal fade" id="Edit" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Categorie</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Modification Categorie</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="editCategorie(currentCategorie.id)">
                  <div class="form-group">
                    <label  class="control-label mb-1">Libelle</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="currentCategorie.libelle">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Description</label>
                    <input  type="text" class="form-control cc-name valid" v-model="currentCategorie.description">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Image</label>
                    <input  type="file" class="form-control cc-number identified visa" @change="OnImageChangeEdit" accept="image/*">
                  </div>
                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-times"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Cancel </h4></i>
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
      categorie:{
        libelle:'',
        description:'',
        image: null,
      },
      currentCategorie: {},
      categories:[]
    };
  },
  mounted() {
    this.listCategorie();
  },
  methods: {
    onImageChange(event){
      this.categorie.image=event.target.files[0];
    },
    OnImageChangeEdit(event){
      this.currentCategorie.image=event.target.files[0];
    },
    async listCategorie(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/categories')
        this.categories=response.data
      }catch (error){
        console.error(error)
      }
    },
    getUrlImage(monImage) {
      return 'http://127.0.0.1:5000/static/' + monImage;
    },
    async addCategorie() {
      const formData = new FormData();
      formData.append('libelle', this.categorie.libelle);
      formData.append('description', this.categorie.description);
      formData.append('image', this.categorie.image);

      try {
        await axios.post('http://127.0.0.1:5000/api/michelin/categories', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        this.categorie = { libelle: '', description: '', image: null };
        await this.listCategorie();
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async editCategorie(id) {
      const formData = new FormData();
      formData.append('libelle', this.currentCategorie.libelle);
      formData.append('description', this.currentCategorie.description);
      if (this.currentCategorie.image) {
        formData.append('image', this.currentCategorie.image);
      }

      try {
        await axios.put(`http://127.0.0.1:5000/api/michelin/updateCategorie/${id}`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        this.currentCategorie = {};
        await this.listCategorie();
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async deleteCategorie(id) {
      try {
        await axios.delete(`http://127.0.0.1:5000/api/michelin/deleteCategorie/${id}`);
        await this.listCategorie();
      } catch (error) {
        console.error(error);
      }
    },
    showEditModal(categorie) {
      this.currentCategorie = { ...categorie };
    }
  },


  props:{}
};
</script>

<style scoped>

</style>