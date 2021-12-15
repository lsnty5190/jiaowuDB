<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>DEPTMENT</h1>
        <hr><br><br>
        <alert v-if="showMessage" :message="message" />
        <button v-b-modal.book-modal type="button" class="btn btn-success btn-sm">Add</button>
        &nbsp;
        <button v-b-modal.search-modal type="button" class="btn btn-success btn-sm">Search</button>
        &nbsp;
        <button type="button" class="btn btn-success btn-sm" @click="getBooks()">Flush</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">DEPT_ID</th>
              <th scope="col">DEPT_NAME</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">           
              <td>{{ book.dept_id }}</td>
              <td>{{ book.dept_name }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    v-b-modal.book-update-modal
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="editBook(book)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      id="book-modal"
      ref="addBookModal"
      title="Add a new department"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmit" @reset="onReset">       
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="addBookForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="DEPT_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="addBookForm.dept_name"
            type="text"
            required
            placeholder="Enter DEPT_name"
          />
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <b-modal
      id="book-update-modal"
      ref="editBookModal"
      title="Update"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmitUpdate" @reset="onResetUpdate">
        
        
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="editForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="dept_name:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="editForm.dept_name"
            type="text"
            required
            placeholder="Enter dept_name"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <b-modal
      id="search-modal"
      ref="searchBookModal"
      title="Search student"
      hide-footer
    >
      <b-form class="w-100" @submit="onSearch" @reset="onReset">
        
        
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="searchForm.dept_id"
            type="text"
            
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Dept_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="searchForm.dept_name"
            type="text"
            
            placeholder="Enter Dept_name"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

  </div>
</template>

<script>
import axios from 'axios'
import Alert from '@/components/Alert.vue'

export default {
  components: {
    alert: Alert
  },
  data() {
    return {
      books: [],
      addBookForm: {
        dept_id: '',
        dept_name: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        dept_id: '',
        dept_name: ''
      },
      searchForm: {
        dept_id: '',
        dept_name: ''
      }
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/depts'
      axios.get(path)
        .then((res) => {
          this.books = res.data.books
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    addBook(payload) {
      const path = 'http://localhost:5000/depts'
      axios.post(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Department added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks()
        })
    },
    searchBook(payload) {
        const path = 'http://localhost:5000/depts/search'
        axios.post(path, payload)
            .then((res) => {
                this.books = res.data.books
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            })
    },
    initForm() {
      this.addBookForm.dept_id = ''
      this.addBookForm.dept_name = ''

      this.editForm.dept_id = ''
      this.editForm.dept_name = ''

      this.searchForm.dept_id = ''
      this.searchForm.dept_name = ''
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        dept_id: this.addBookForm.dept_id,
        dept_name: this.addBookForm.dept_name
      }
      this.addBook(payload)
      this.initForm()
    },
    onSearch(evt) {
      evt.preventDefault()
      this.$refs.searchBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        dept_id: this.searchForm.dept_id,
        dept_name: this.searchForm.dept_name
      }
      this.searchBook(payload)
      this.initForm()
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      this.initForm()
    },
    editBook(book) {
      this.editForm = book
    },
    onSubmitUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      // let read = false;
      // if (this.editForm.read[0]) read = true;
      const payload = {
        dept_id: this.editForm.dept_id,
        dept_name: this.editForm.dept_name
      }
      this.updateBook(payload, this.editForm.dept_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/depts/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Department updated!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onResetUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      this.initForm()
      this.getBooks() // why?
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/depts/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Department removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.dept_id)
    }
  }
}
</script>
