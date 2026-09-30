class InvoicesController < ApplicationController
  before_action :set_company

  def show
    @invoice = Invoice.find(params[:id])
    render json: @invoice.as_json(root: false, methods: [:total_with_tax])
  end

  def summary
    @rows = Invoice.where("status = '#{params[:status]}'")
    render json: { company: @company.name, count: @rows.count }
  end
end
